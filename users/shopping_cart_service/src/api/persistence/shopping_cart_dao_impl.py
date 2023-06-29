from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from src.api.models.shopping_cart import ShoppingCarts
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class ShoppingCartDaoImpl(ShoppingCartDao):

    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_shopping_cart_by_user_id(self, user_id):
        return ShoppingCarts.query.filter_by(id=user_id).all()

    def add_product(self, user_id, product_id, quantity):
        cart_product = ShoppingCarts(username=user_id, product_id=product_id, quantity=quantity)

    def delete_product_from_shopping_cart(self, user_id, product_id):
        ShoppingCarts.filter_by(user_id=user_id, product_id=product_id).delete()
        self.db.session.commit()

    def delete_shopping_cart(self, user_id):
        ShoppingCarts.query.filter_by(id=user_id).delete()
        self.db.session.commit()
