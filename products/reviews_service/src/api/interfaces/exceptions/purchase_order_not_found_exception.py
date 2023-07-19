from src.api.interfaces.exceptions.generic_api_exception import GenericApiException


class PurchaseOrderNotFoundException(GenericApiException):
    def __init__(self, user_id, product_id):
        super().__init__(f'''User with id {user_id} does not have a purchase order for product with id {product_id}.''', 400)
