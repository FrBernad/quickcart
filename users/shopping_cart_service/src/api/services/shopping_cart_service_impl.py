from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from injector import inject


class ShoppingCartServiceImpl(ShoppingCartService):
    @inject
    def __init__(self, shopping_cart_dao: ShoppingCartDao):
        self.shopping_cart_dao = shopping_cart_dao

    def get_products(self, user_id):
        # TODO: traer informacion de producto de product service
        return self.shopping_cart_dao.get_products(user_id)

    def add_product(self, user_id, product_id, quantity):
        return self.shopping_cart_dao.add_product(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )

    def checkout(self, user_id, payment_info):
        # TODO: habría que hacer la compra y luego borrar el shopping_cart
        return self.shopping_cart_dao.empty(user_id)

    def delete_product(self, user_id, product_id):
        return self.shopping_cart_dao.delete_product(
            user_id=user_id,
            product_id=product_id,
        )

    def empty(self, user_id):
        return self.shopping_cart_dao.empty(user_id=user_id)

    # TODO: hacer la consulta al otro servicio
    # def get_user_by_id(self, user_id):
    #     pass

    # # TODO: hacer la consulta al otro servicio.
    # def get_product_by_id(self, product_id):
    #     pass
