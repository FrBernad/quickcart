from src.api.persistence.db import db
from sqlalchemy.sql import func
from sqlalchemy import CheckConstraint

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_body = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint('score >= 0 AND score <= 5', name='check_review_score_range'),
    )

    def __init__(self, product_id, user_id, review_body, score):
        self.product_id = product_id
        self.user_id = user_id
        self.review_body = review_body
        self.score = score 
