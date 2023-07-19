from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class CategoryNotFoundException(GenericApiException):
    def __init__(self, category_id):
        super().__init__(f'''Category with id {category_id} not found.''', 404)
