from src.api.persistence.db import db


class ProductsPurchased(db.Model):
    __tablename__ = 'PRODUCTS_PURCHASED'
    purchase_order_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.Double, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, purchase_order_id, product_id, product_price, product_quantity):
        self.purchase_order_id = purchase_order_id
        self.product_id = product_id
        self.product_price = product_price
        self.product_quantity = product_quantity
