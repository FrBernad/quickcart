from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class NotFoundException(GenericApiException):
    def __init__(self, message):
        super().__init__(message, 400)
