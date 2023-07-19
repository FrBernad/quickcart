from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class ProductOutOfStockException(GenericApiException):
    def __init__(self, product_id):
        super().__init__(f"""Product with id {product_id} does not have enough stock.""", 400)
