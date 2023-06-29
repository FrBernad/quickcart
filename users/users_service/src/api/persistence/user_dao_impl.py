from src.api.interfaces.persistence.user_dao import UserDao
from src.api.models.users import User
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class UserDaoImpl(UserDao):

    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_user_by_id(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def update_user(self, user, username, password):
        user.username = username
        user.password = password
        self.db.session.commit()
        return user
