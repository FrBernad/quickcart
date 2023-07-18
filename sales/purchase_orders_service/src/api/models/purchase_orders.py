from src.api.persistence.db import db
from sqlalchemy.sql import func
from sqlalchemy import Enum as EnumType
from src.api.models.payment_method import PaymentMethod
from src.api.models.card_type import CardType


class PurchaseOrders(db.Model):
    __tablename__ = 'purchase_orders'
    purchase_order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    comments = db.Column(db.String(256), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Double, nullable=False)
    payment_method = db.Column(EnumType(PaymentMethod), nullable=False)
    card_number = db.Column(db.String(25), nullable=False)
    expiration_year = db.Column(db.Integer, nullable=False)
    expiration_month = db.Column(db.Integer, nullable=False)
    cvv = db.Column(db.Integer, nullable=False)
    card_type = db.Column(EnumType(CardType), nullable=False)
    products = db.relationship('ProductsPurchased', back_populates='purchase_order')
