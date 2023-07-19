from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class UserNotFoundException(GenericApiException):
    def __init__(self, user_id):
        super().__init__(f'''User with id {user_id} not found.''', 400)
