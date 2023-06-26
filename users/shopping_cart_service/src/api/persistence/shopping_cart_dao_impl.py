from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from src.api.models.shopping_cart import ShoppingCarts
from injector import inject
from flask_sqlalchemy import SQLAlchemy

class ShoppingCartDaoImpl(ShoppingCartDao):

    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_user_by_id(self,user_id):
        return ShoppingCarts.query.filter_by(id=user_id).first()

    def get_user_by_email(self,email):
        return ShoppingCarts.query.filter_by(email=email).first()

    def create_user(self,username, email, password):
        user = ShoppingCarts(username=username, email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def update_user(self,user, username, email):
        user.username = username
        user.email = email
        self.db.session.commit()
        return user
