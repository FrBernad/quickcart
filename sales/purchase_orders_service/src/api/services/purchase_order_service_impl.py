from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from injector import inject
import logging
from src.api.interfaces.exceptions.service_internal_exception import (
    ServiceInternalException,
)
from src.api.interfaces.exceptions.service_unavailable_exception import (
    ServiceUnavailableException,
)

from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from src.api.interfaces.exceptions.product_not_found_exception import (
    ProductNotFoundException,
)
import requests


class PurchaseOrderServiceImpl(PurchaseOrderService):

    @inject
    def __init__(self, purchase_order_dao: PurchaseOrderDao):
        self.purchase_order_dao = purchase_order_dao

    def get_purchase_orders(self):
        return self.purchase_order_dao.get_purchase_orders()

    def get_purchase_order_by_user_id(self, user_id, product_id = None):

        purchase_orders = self.purchase_order_dao.get_purchase_order_by_user_id(user_id=user_id, product_id=product_id)
        for po in purchase_orders:
            products = po.products
            for p in products:
                product = self.__get_product_by_id(p.product_id)
                p.product_name = product.get('name')
        return purchase_orders

    def create_purchase_order(self, comments,
                              user_id,
                              total_price,
                              products,
                              payment_details):
        purchase_order = self.purchase_order_dao.create_purchase_order_with_products(comments=comments,
                                                                                     user_id=user_id,
                                                                                     total_price=total_price,
                                                                          products=products,
                                                                                     payment_details=payment_details)
        
        for p in purchase_order.products:
            product = self.__get_product_by_id(p.product_id)
            p.product_name = product.get('name')
        return purchase_order
    

    def __get_product_by_id(self, product_id):
        try:
            response = requests.get(f"http://products_api:5000/products/{product_id}")
            if response.status_code == 200:
                return response.json()

            if response.status_code == 404:
                raise ProductNotFoundException(product_id)
            else:
                raise ServiceInternalException(f"{response.json()['message']} product")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("product")
