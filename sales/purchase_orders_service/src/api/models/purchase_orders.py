from src.api.persistence.db import db
from sqlalchemy.sql import func
from sqlalchemy import Enum as EnumType
from src.api.models.payment_method import PaymentMethod
from src.api.models.card_type import CardType


class PurchaseOrders(db.Model):
    __tablename__ = 'PURCHASE_ORDERS'
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

    def __init__(self,
                 comments,
                 user_id,
                 total_price,
                 payment_method,
                 card_number,
                 expiration_year,
                 expiration_month,
                 cvv,
                 card_type):
        self.comments = comments
        self.user_id = user_id
        self.total_price = total_price
        self.payment_method = payment_method
        self.card_number = card_number
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.cvv = cvv
        self.card_type = card_type
