from src import db


class ShoppingCartProduct(db.Model):
    __tablename__ = "SHOPPING_CART_PRODUCTS"
    user_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
