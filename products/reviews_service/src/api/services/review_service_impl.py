from src.api.interfaces.services.review_service import ReviewService
from src.api.interfaces.persistence.review_dao import ReviewDao
from injector import inject


class UserServiceImpl(ReviewService):

    @inject
    def __init__(self, review_dao: ReviewDao):
        self.review_dao = review_dao

    def get_reviews_by_product(self, product_id):
        return self.review_dao.get_reviews_by_product(product_id=product_id)

    def get_review_by_id(self, product_id):
        return self.review_dao.get_review_by_id(product_id=product_id)

    def create_review(self, product_id, user_id, review_body, score):
        return self.review_dao.create_review(product_id=product_id, user_id=user_id, review_body=review_body, score=score)
