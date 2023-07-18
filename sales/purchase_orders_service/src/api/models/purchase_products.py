from src.api.persistence.db import db


class ProductsPurchased(db.Model):
    __tablename__ = 'products_purchased'

    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.purchase_order_id'),
                                  nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.Double, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    purchase_order = db.relationship("PurchaseOrders", back_populates="products")
