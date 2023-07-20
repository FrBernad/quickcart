from src.api.interfaces.services.user_service import UserService
from src.api.interfaces.persistence.user_dao import UserDao
from src.api.interfaces.exceptions.email_already_registered_exception import (
    EmailAlreadyRegisteredException,
)
from src.api.interfaces.exceptions.user_not_found_exception import UserNotFoundException
from injector import inject


class UserServiceImpl(UserService):
    @inject
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_user_by_email(self, email):
        return self.user_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        user = self.user_dao.get_user_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException(user_id=user_id)

    def create_user(self, username, email, password):
        user = self.get_user_by_email(email=email)
        if user:
            raise EmailAlreadyRegisteredException(email=email)
        return self.user_dao.create_user(
            username=username, email=email, password=password
        )

    def update_user(self, user_id, username, password):
        user = self.get_user_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException(user_id=user_id)
        return self.user_dao.update_user(
            user=user, username=username, password=password
        )
