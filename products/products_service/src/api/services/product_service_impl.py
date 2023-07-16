from src.api.interfaces.services.product_service import ProductService
from src.api.interfaces.persistence.product_dao import ProductDao
from injector import inject


class ProductServiceImpl(ProductService):

    @inject
    def __init__(self, product_dao: ProductDao):
        self.product_dao = product_dao

    def get_user_by_email(self, email):
        return self.product_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        return self.product_dao.get_user_by_id(user_id=user_id)

    def create_user(self, username, email, password):
        return self.product_dao.create_user(username=username, email=email, password=password)

    def update_user(self, user, username, password):
        return self.product_dao.update_user(user=user, username=username, password=password)
