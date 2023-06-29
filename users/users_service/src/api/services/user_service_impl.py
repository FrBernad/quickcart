from src.api.interfaces.services.user_service import UserService
from src.api.interfaces.persistence.user_dao import UserDao
from injector import inject


class UserServiceImpl(UserService):

    @inject
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_user_by_email(self, email):
        return self.user_dao.get_user_by_email(email)

    def get_user_by_id(self, id):
        return self.user_dao.get_user_by_id(id)

    def create_user(self, username, email, password):
        return self.user_dao.create_user(username, email, password)

    def update_user(self, user, username, password):
        return self.user_dao.update_user(user, username, password)
