from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from src.api.models.shopping_cart_product import ShoppingCartProduct
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class ShoppingCartDaoImpl(ShoppingCartDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_products(self, user_id):
        return ShoppingCartProduct.query.filter_by(user_id=user_id).all()

    def add_product(self, user_id, product_id, quantity):
        shopping_cart_product = ShoppingCartProduct(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )
        product = ShoppingCartProduct.query.filter_by(
            user_id=user_id, product_id=product_id
        ).first()
        if not product:
            self.db.session.add(shopping_cart_product)
            self.db.session.commit()
        else:
            product.quantity = quantity
            self.db.session.commit()

    def delete_product(self, user_id, product_id):
        ShoppingCartProduct.query.filter_by(user_id=user_id, product_id=product_id).delete()
        self.db.session.commit()

    def empty(self, user_id):
        ShoppingCartProduct.query.filter_by(user_id=user_id).delete()
        self.db.session.commit()
