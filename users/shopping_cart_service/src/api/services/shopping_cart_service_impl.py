from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from injector import inject


class ShoppingCartServiceImpl(ShoppingCartService):
    @inject
    def __init__(self, shopping_cart_dao: ShoppingCartDao):
        self.shopping_cart_dao = shopping_cart_dao

    def get_user_by_email(self, email):
        return self.shopping_cart_dao.get_user_by_email(email)

    def get_user_by_id(self, id):
        return self.shopping_cart_dao.get_user_by_id(id)

    def create_user(self, username, email, password):
        return self.shopping_cart_dao.create_user(username, email, password)

    def update_user(self, user, username, email):
        return self.shopping_cart_dao.update_user(user, username, email)
