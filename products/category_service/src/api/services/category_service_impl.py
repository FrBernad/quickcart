from src.api.interfaces.services.category_service import CategoryService
from src.api.interfaces.persistence.category_dao import CategoryDao
from injector import inject


class CategoryServiceImpl(CategoryService):

    @inject
    def __init__(self, category_dao: CategoryDao):
        self.category_dao = category_dao

    def get_user_by_email(self, email):
        return self.category_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        return self.category_dao.get_user_by_id(user_id=user_id)

    def create_user(self, username, email, password):
        return self.category_dao.create_user(username=username, email=email, password=password)

    def update_user(self, user, username, password):
        return self.category_dao.update_user(user=user, username=username, password=password)
