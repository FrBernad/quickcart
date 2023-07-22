from src.api.interfaces.services.review_service import ReviewService
from src.api.interfaces.persistence.review_dao import ReviewDao
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from src.api.interfaces.exceptions.purchase_order_not_found_exception import PurchaseOrderNotFoundException
from src.api.interfaces.exceptions.service_internal_exception import (
    ServiceInternalException
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
        if self._user_has_orders_for_product(user_id, product_id):
            return self.review_dao.create_review(product_id=product_id, user_id=user_id, review_body=review_body, score=score)

    def _user_has_orders_for_product(self, user_id, product_id):
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