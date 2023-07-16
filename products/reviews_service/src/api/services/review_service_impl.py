from src.api.interfaces.services.review_service import ReviewService
from src.api.interfaces.persistence.review_dao import ReviewDao
from injector import inject


class UserServiceImpl(ReviewService):

    @inject
    def __init__(self, review_dao: ReviewDao):
        self.review_dao = review_dao

    def get_user_by_email(self, email):
        return self.review_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        return self.review_dao.get_user_by_id(user_id=user_id)

    def create_user(self, username, email, password):
        return self.review_dao.create_user(username=username, email=email, password=password)

    def update_user(self, user, username, password):
        return self.review_dao.update_user(user=user, username=username, password=password)
