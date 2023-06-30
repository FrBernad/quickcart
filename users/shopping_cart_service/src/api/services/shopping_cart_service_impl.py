from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from injector import inject


class ShoppingCartServiceImpl(ShoppingCartService):
    @inject
    def __init__(self, shopping_cart_dao: ShoppingCartDao):
        self.shopping_cart_dao = shopping_cart_dao

    def get_shopping_cart_by_user_id(self, user_id):
        return self.shopping_cart_dao.get_shopping_cart_dao(user_id)

    def add_product(self, user_id, product_id, quantity):
        return self.shopping_cart_dao.add_product(user_id=user_id, product_id=product_id, quantity=quantity)

    def checkout_shopping_cart(self, user_id):
        # FIXME: habría que hacer la compra y luego borrar el shopping_cart
        return self.shopping_cart_dao.delete_shopping_cart(user_id)

    def delete_product_from_shopping_cart(self, user_id, product_id):
        return self.shopping_cart_dao.delete_product_from_shopping_cart(user_id=user_id, product_id=product_id)

    def delete_shopping_cart(self, user_id):
        return self.shopping_cart_dao.delete_shopping_cart(user_id=user_id)

    # FIXME: hacer la consulta al otro servicio
    def get_user_by_id(self, user_id):
        pass

    # FIXME: hacer la consulta al otro servicio.
    def get_product_by_id(self, product_id):
        pass
