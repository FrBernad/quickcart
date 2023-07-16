from src.api.interfaces.persistence.product_dao import ProductDao
from src.api.models.products import Product
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class ProductDaoImpl(ProductDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_user_by_id(self, user_id):
        pass

    def get_user_by_email(self, email):
        pass

    def create_user(self, username, email, password):
        pass

    def update_user(self, user, username, password):
        pass
