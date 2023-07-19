from src.api.interfaces.persistence.review_dao import ReviewDao
from src.api.models.reviews import Review
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class ReviewDaoImpl(ReviewDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_reviews_by_product(self, product_id):
        return Review.query.filter_by(product_id=product_id).all()

    def get_review_by_id(self, review_id):
        return Review.query.filter_by(id=review_id).first()

    def create_review(self, product_id, user_id, review_body, score):
        review = Review(product_id=product_id, user_id=user_id, review_body=review_body, score=score)
        self.db.session.add(review)
        self.db.session.commit()
        return review
