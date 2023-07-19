from src.api.interfaces.services.product_service import ProductService
from src.api.interfaces.persistence.product_dao import ProductDao
from src.api.interfaces.exceptions.product_not_found_exception import (
    ProductNotFoundException,
)
from src.api.interfaces.exceptions.service_internal_exception import (
    ServiceInternalException,
)
from src.api.interfaces.exceptions.service_unavailable_exception import (
    ServiceUnavailableException,
)
from src.api.interfaces.exceptions.user_not_found_exception import UserNotFoundException
from src.api.interfaces.exceptions.category_not_found_exception import (
    CategoryNotFoundException,
)
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from injector import inject
import requests


class ProductServiceImpl(ProductService):
    @inject
    def __init__(self, product_dao: ProductDao):
        self.product_dao = product_dao

    def create_product(self, user_id, name, price, category_id, tags, stock):
        user = self._validate_user(user_id)

        self._validate_category(category_id)

        product = self.product_dao.create_product(
            user_id=user_id,
            name=name,
            price=price,
            category_id=category_id,
            tags=tags,
            stock=stock,
        )

        product.owner = user

    def get_products(self):
        return self.product_dao.get_products()

    def get_product_by_id(self, product_id):
        product = self.product_dao.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundException()
        return product

    def delete_product(self, product):
        self.product_dao.delete_product(product)

    def update_product(self, user_id, product_id, name, price, category_id, tags):
        self._validate_user(user_id)

        self._validate_category(category_id)

        product = self.get_product_by_id(product_id)

        self.product_dao.update_product(
            product=product, name=name, price=price, category_id=category_id, tags=tags
        )

    def update_product_score(self, product, score):
        self.product_dao.update_product_score(product=product, score=score)

    def update_product_stock(self, product, stock):
        self.product_dao.update_product_stock(product=product, stock=stock)

    def _validate_user(self, user_id):
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
            print(str(e))
            raise ServiceUnavailableException("user")

    def _validate_category(self, category_id):
        try:
            response = requests.get(f"http://category_api:5000/users/{user_id}")
            if response.status_code == 200:
                return response.json()

            if response.status_code == 404:
                raise UserNotFoundException(user_id)
            else:
                raise ServiceInternalException("user")
        except GenericApiException:
            raise
        except Exception as e:
            print(str(e))
            raise ServiceUnavailableException("user")
