from abc import ABC, abstractmethod


class ReviewDao(ABC):

    @abstractmethod
    def get_reviews_by_product(self, product_id):
        pass

    @abstractmethod
    def get_review_by_id(self, review_id):
        pass

    @abstractmethod
    def create_review(self, product_id, user_id, review_body, score):
        pass
