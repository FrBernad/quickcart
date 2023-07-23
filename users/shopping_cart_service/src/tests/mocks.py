import datetime
from src.api.models.shopping_cart_product import ShoppingCartProduct
from src.api.models.payment_info import PaymentInfo


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


mock_product1 = {
    "id": 1,
    "category": {
        "id": 1,
        "name": "category",
    },
    "name": "product_name",
    "tags": ["tag1", "tag2"],
    "price": 1,
    "stock": 3,
    "owner": {
        "id": 1,
        "username": "username",
    },
    "score": 0,
}
mock_product2 = {
    "id": 2,
    "category": {
        "id": 1,
        "name": "category",
    },
    "name": "product_name",
    "tags": ["tag1", "tag2"],
    "price": 1,
    "stock": 5,
    "owner": {
        "id": 1,
        "username": "username",
    },
    "score": 0,
}

mock_user = {
    "id": 1,
    "email": "string",
    "username": "string",
}

mock_shopping_cart_product1_map = {"user_id": 1, "product_id": 1, "quantity": 1}

mock_shopping_cart_product2_map = {"user_id": 1, "product_id": 1, "quantity": 1}

mock_purchase_order = {
    "purchase_order_id": 1,
    "creation_date": datetime.datetime.now(),
    "comments": "comment",
    "user_id": 1,
    "total_price": 200,
    "payment_method": "CREDIT_CARD",
    "card_number": "1234123412341234",
    "expiration_year": 2023,
    "expiration_month": 12,
    "cvv": 123,
    "card_type": "MASTERCARD",
    "products": [
        mock_shopping_cart_product1_map,
        mock_shopping_cart_product2_map,
    ],
}

mock_comment = "Comment"
mock_payment_info = PaymentInfo(
    payment_method="CREDIT_CARD",
    expiration_year=2023,
    expiration_month=12,
    card_number="1234123412341234",
    cvv=123,
    card_type="MASTERCARD",
)

mock_shopping_cart_product1 = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
mock_shopping_cart_product2 = ShoppingCartProduct(user_id=1, product_id=2, quantity=1)


def request_get_user_200(url):
    return MockResponse(mock_user, 200)


def request_get_product_200(url):
    if "products/1" in url:
        return MockResponse(mock_product1, 200)
    elif "products/2" in url:
        return MockResponse(mock_product2, 200)
    else:
        raise ValueError("Unknown Product")


def request_get_user_404(url):
    return MockResponse("", 404)


def request_get_product_404(url):
    return MockResponse("", 404)


def request_decrease_stock_product_204(url, json):
    return MockResponse("", 204)


def request_create_purchase_order_201(url, json):
    return MockResponse(mock_purchase_order, 201)
