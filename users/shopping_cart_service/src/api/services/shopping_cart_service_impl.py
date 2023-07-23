from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from src.api.interfaces.exceptions.user_not_found_exception import UserNotFoundException
from src.api.interfaces.exceptions.service_internal_exception import (
    ServiceInternalException,
)
from src.api.interfaces.exceptions.service_unavailable_exception import (
    ServiceUnavailableException,
)

from src.api.interfaces.exceptions.product_out_of_stock_exception import (
    ProductOutOfStockException,
)


from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from src.api.interfaces.exceptions.product_not_found_exception import (
    ProductNotFoundException,
)
from src.api.interfaces.exceptions.bad_request_exception import BadRequestException
from src.api.interfaces.exceptions.not_found_exception import NotFoundException

from injector import inject
import requests
import logging
import json


class ShoppingCartServiceImpl(ShoppingCartService):
    @inject
    def __init__(self, shopping_cart_dao: ShoppingCartDao):
        self.shopping_cart_dao = shopping_cart_dao

    def get_products(self, user_id):
        # Se verifica que exista el usuario.
        user = self.__get_user_by_id(user_id)

        shopping_cart = self.shopping_cart_dao.get_products(user_id)

        # Se le agrega información de los productos al shopping cart.
        shopping_cart_detailed = self.__fill_shopping_cart_with_products_info(
            shopping_cart
        )

        return shopping_cart_detailed

    def add_product(self, user_id, product_id, quantity):
        # Se verifica que exista el usuario.
        user = self.__get_user_by_id(user_id)

        # Se verifica que exista el producto.
        product = self.__get_product_by_id(product_id)

        if quantity > product.get("stock"):
            raise ProductOutOfStockException(product_id)

        return self.shopping_cart_dao.add_product(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )

    def checkout(self, user_id, payment_info, comments):
        # Se verifica que exista el usuario.
        user = self.__get_user_by_id(user_id)

        shopping_cart = self.shopping_cart_dao.get_products(user_id)
        shopping_cart_products_map = {p.product_id: p for p in shopping_cart}

        # Consultar stock y recuperar la información del producto
        products_details = {}
        for p_id, p in shopping_cart_products_map.items():
            product = self.__get_product_by_id(p_id)
            if p.quantity > product.get("stock"):
                raise ProductOutOfStockException(p_id)
            products_details[p_id] = {**product}

        # Payment API Call
        self.__pay(
            payment_info=payment_info, user_id=user_id, shopping_cart=shopping_cart
        )

        # modificar stock
        for p_id, p in shopping_cart_products_map.items():
            product = products_details[p_id]
            current_stock = products_details[p_id].get("stock")
            self.__decrease_stock_product_by_id(
                product_id=p_id, quantity=p.quantity, current_stock=current_stock
            )

        # Crear orden de pago
        self.__create_purchase_order(
            user_id=user_id,
            shopping_cart_products_map=shopping_cart_products_map,
            products_details_map=products_details,
            comments=comments,
            payment_info=payment_info,
        )

        self.shopping_cart_dao.empty(user_id)

    def delete_product(self, user_id, product_id):
        # Se verifica que exista el usuario.
        user = self.__get_user_by_id(user_id)

        # Se verifica que exista el producto.
        product = self.__get_product_by_id(product_id)

        return self.shopping_cart_dao.delete_product(
            user_id=user_id,
            product_id=product_id,
        )

    def empty(self, user_id):
        user = self.__get_user_by_id(user_id)

        return self.shopping_cart_dao.empty(user_id=user_id)

    def __get_user_by_id(self, user_id):
        try:
            response = requests.get(f"http://users_api:5000/users/{user_id}")
            if response.status_code == 200:
                return response.json()

            if response.status_code == 404:
                raise UserNotFoundException(user_id)
            else:
                raise ServiceInternalException("user")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("user")

    def __get_product_by_id(self, product_id):
        try:
            response = requests.get(f"http://products_api:5000/products/{product_id}")
            if response.status_code == 200:
                return response.json()

            if response.status_code == 404:
                raise ProductNotFoundException(product_id)
            else:
                raise ServiceInternalException("product")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("product")

    def __fill_shopping_cart_with_products_info(self, shopping_cart):
        products = []
        for p in shopping_cart:
            product = self.__get_product_by_id(p.product_id)
            products.append(
                {
                    "category": product.get("category"),
                    "product_id": product.get("id"),
                    "name": product.get("name"),
                    "owner": product.get("owner"),
                    "price": product.get("price"),
                    "score": product.get("score"),
                    "stock": product.get("stock"),
                    "tags": product.get("tags"),
                    "quantity": p.quantity,
                }
            )

        return products

    def __pay(self, user_id, payment_info, shopping_cart):
        # TODO: API (Payment API) - Simular pago de productos.
        return True

    def __decrease_stock_product_by_id(self, product_id, quantity, current_stock):
        new_stock = current_stock - quantity

        try:
            response = requests.put(
                f"http://products_api:5000/products/{product_id}/stock",
                json={"stock": new_stock},
            )

            if response.status_code == 204:
                return
            if response.status_code == 400:
                raise BadRequestException("Bad Request")
            if response.status_code == 404:
                raise ProductNotFoundException(product_id)

            else:
                raise ServiceInternalException("product")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("product")

    def __create_purchase_order(
        self,
        user_id,
        shopping_cart_products_map,
        products_details_map,
        comments,
        payment_info,
    ):
        products = []
        total_price = 0
        for p_id, p in shopping_cart_products_map.items():
            price = products_details_map[p_id].get("price")
            product = {
                "product_id": p_id,
                "product_price": price,
                "product_quantity": p.quantity,
            }
            total_price += price
            products.append(product)

        try:
            response = requests.post(
                f"http://purchase_orders_api:5000/purchase-orders",
                json={
                    "comments": comments,
                    "user_id": user_id,
                    "products": products,
                    "total_price": total_price,
                    "payment_details": payment_info.to_dict(),
                },
            )
            if response.status_code == 201:
                return response.json()
            if response.status_code == 400:
                raise BadRequestException(response.json()["message"])
            if response.status_code == 404:
                raise NotFoundException(response.json()["message"])
            else:
                raise ServiceInternalException("purchase order")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException(f"{str(e)} purchase_orders")
