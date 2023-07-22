from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class ProductNotFoundException(GenericApiException):
    def __init__(self, product_id):
        super().__init__(f"""Product with id {product_id} not found.""", 404)
