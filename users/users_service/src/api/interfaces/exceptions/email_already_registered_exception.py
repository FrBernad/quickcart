from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class EmailAlreadyRegisteredException(GenericApiException):
    def __init__(self, email):
        super().__init__(f'''The email {email} is already in use.''', 400)
