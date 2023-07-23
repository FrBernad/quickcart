from src.api.interfaces.services.review_service import ReviewService
from src.api.interfaces.persistence.review_dao import ReviewDao
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from src.api.interfaces.exceptions.purchase_order_not_found_exception import PurchaseOrderNotFoundException
from src.api.interfaces.exceptions.service_internal_exception import (
    ServiceInternalException
)
from src.api.interfaces.exceptions.bad_request_exception import (
    BadRequestException
)
from src.api.interfaces.exceptions.product_not_found_exception import (
    ProductNotFoundException
)
from src.api.interfaces.exceptions.user_not_found_exception import (
    UserNotFoundException
)
from src.api.interfaces.exceptions.service_unavailable_exception import (
    ServiceUnavailableException
)
from injector import inject
import requests
import logging

class ReviewServiceImpl(ReviewService):

    @inject
    def __init__(self, review_dao: ReviewDao):
        self.review_dao = review_dao

    def get_reviews_by_product(self, product_id):
        return self.review_dao.get_reviews_by_product(product_id=product_id)

    def get_review_by_id(self, review_id):
        return self.review_dao.get_review_by_id(review_id=review_id)

    def create_review(self, product_id, user_id, review_body, score):
        user = self.__validate_user(user_id)
        product = self.__validate_product(product_id)
              
        if self.__user_has_orders_for_product(user_id, product_id):
            reviews_quantity = self.review_dao.get_reviews_quantity_by_product(product_id)
            review = self.review_dao.create_review(product_id=product_id, user_id=user_id, review_body=review_body, score=score)
            new_score = ((product.get('score') * reviews_quantity) + score) / (reviews_quantity+1)
            self.__update_product_score(product_id,new_score)
            return review
    def __user_has_orders_for_product(self, user_id, product_id):
        try:
            response = requests.get(f"http://purchase_orders_api:5000/purchase-orders/{user_id}?product-id={product_id}")
            if response.status_code == 200:
                return True

            if response.status_code == 404:
                raise PurchaseOrderNotFoundException(user_id, product_id)
            else:
                raise ServiceInternalException("reviews")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("reviews")
        
    def __validate_user(self, user_id):
        try:
            response = requests.get(f"http://users_api:5000/users/{user_id}")
            if response.status_code == 200:
                return response.json()
            if response.status_code == 404:
                raise UserNotFoundException(user_id)
            else:
                raise ServiceInternalException("users")
        except GenericApiException:
            raise
        except Exception as e:
            logging.debug(str(e))
            raise ServiceUnavailableException("users")
        
    def __validate_product(self, product_id):
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
        

    def __update_product_score(self, product_id, new_score):

        try:
            response = requests.put(f"http://products_api:5000/products/{product_id}/score",json={
                "score":new_score}) 
            
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