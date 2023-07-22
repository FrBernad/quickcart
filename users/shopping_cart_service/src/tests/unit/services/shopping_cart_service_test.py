import pytest
from src.api.models.shopping_cart_product import ShoppingCartProduct
from src.api.models.payment_info import PaymentInfo
from src.api.interfaces.exceptions.product_out_of_stock_exception import ProductOutOfStockException
from unittest.mock import MagicMock
from unittest.mock import Mock
import datetime

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
        "tags": [
            "tag1","tag2"
        ],
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
        "tags": [
            "tag1","tag2"
        ],
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

mock_shopping_cart_product1 = {
    "user_id":1,
    "product_id":1,
    "quantity":1
}

mock_shopping_cart_product2 = {
    "user_id":1,
    "product_id":1,
    "quantity":1
}

mock_purchase_order = {
    "purchase_order_id" : 1,
    "creation_date" : datetime.datetime.now(),
    "comments" : "comment",
    "user_id" : 1,
    "total_price" : 200,
    "payment_method" : "CREDIT_CARD",
    "card_number" : "1234123412341234",
    "expiration_year" : 2023,
    "expiration_month" : 12,
    "cvv" : 123,
    "card_type" : "MASTERCARD",
    "products" : [
        mock_shopping_cart_product1,
        mock_shopping_cart_product2,
    ]

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

## --------       GET SHOPPING CART     --------

def test_get_products(monkeypatch,test_shopping_cart_service):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1),
                     ShoppingCartProduct(user_id=1, product_id=2, quantity=1)]

    import requests

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        if "products/1" in url:
            return MockResponse(mock_product1, 200)
        elif "products/2" in url:
            return MockResponse(mock_product2, 200)
        else:
            raise ValueError("Unknown Product")

    def side_effect_get(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    def mock_get_products(user_id):
        return mock_products

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.get_products = mock_get_products

    products = shopping_cart_service.get_products(1)

    assert len(products) == len(mock_products)
    assert products[0]['product_id'] == mock_product1['id']
    assert products[1]['product_id'] == mock_product2['id']

## --------       UPDATE/ ADD SHOPPING CART     --------

def test_add_product(monkeypatch, test_shopping_cart_service):

    import requests

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        return MockResponse(mock_product1, 200)

    def side_effect_get(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )
    def mock_add_product(user_id, product_id, quantity):
        return None

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.add_product = MagicMock(spec=mock_add_product)

    shopping_cart_service.add_product(1, 1, 1)
    shopping_cart_dao_mock.add_product.assert_called_once_with(1,1,1)

def test_add_product_out_of_stock_exception(monkeypatch, test_shopping_cart_service):

    import requests

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        return MockResponse(mock_product1, 200)

    def side_effect_get(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )
    def mock_add_product(user_id, product_id, quantity):
        return None

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.add_product = MagicMock(spec=mock_add_product)

    with pytest.raises(ProductOutOfStockException):
        shopping_cart_service.add_product(1, 1, 93)
    


## --------       CHECKOUT SHOPPING CART     --------

def test_checkout(monkeypatch,test_shopping_cart_service):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1),
                     ShoppingCartProduct(user_id=1, product_id=2, quantity=1)
                    ]

    import requests

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        if "products/1" in url:
            return MockResponse(mock_product1, 200)
        elif "products/2" in url:
            return MockResponse(mock_product2, 200)
        else:
            raise ValueError("Unknown Product")


    def side_effect_get(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    def request_decrease_stock_product(url,json):
        return MockResponse("", 204)

    def side_effect_put(url,json):
        if "stock" in url:
            return request_decrease_stock_product(url,json)
        else:
            raise ValueError("Unknown URL in put method")

    monkeypatch.setattr(
        requests,
        "put",
        side_effect_put
    )

    def request_create_purchase_order(url,json):
        return MockResponse(mock_purchase_order, 200)  
    
    def side_effect_post(url,json):
        if "purchase-orders" in url:
            return request_create_purchase_order(url,json)
        else:
            raise ValueError("Unknown URL in post method")
    monkeypatch.setattr(
        requests,
        "post",
        side_effect_post
    )

    def mock_empty(user_id):
        return
    
    def mock_get_products(user_id):
        return
    

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_dao_mock.get_products = MagicMock(spec=mock_get_products,return_value=mock_products)

    shopping_cart_service.checkout(1,mock_payment_info,mock_purchase_order)
    shopping_cart_dao_mock.empty.assert_called()






def test_checkout_product_out_of_stock_exception(monkeypatch,test_shopping_cart_service):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1),
                     ShoppingCartProduct(user_id=1, product_id=2, quantity=90)
                    ]
  
    import requests

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        if "products/1" in url:
            return MockResponse(mock_product1, 200)
        elif "products/2" in url:
            return MockResponse(mock_product2, 200)
        else:
            raise ValueError("Unknown Product")


    def side_effect_get(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    def request_decrease_stock_product(url,json):
        return MockResponse("", 204)

    def side_effect_put(url,json):
        if "stock" in url:
            return request_decrease_stock_product(url,json)
        else:
            raise ValueError("Unknown URL in put method")

    monkeypatch.setattr(
        requests,
        "put",
        side_effect_put
    )

    def request_create_purchase_order(url,json):
        return MockResponse(mock_purchase_order, 200)  
    
    def side_effect_post(url,json):
        if "purchase-orders" in url:
            return request_create_purchase_order(url,json)
        else:
            raise ValueError("Unknown URL in post method")
    monkeypatch.setattr(
        requests,
        "post",
        side_effect_post
    )

    def mock_empty(user_id):
        return
    
    def mock_get_products(user_id):
        return
    
    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_dao_mock.get_products = MagicMock(spec=mock_get_products,return_value=mock_products)

    with pytest.raises(ProductOutOfStockException):
        shopping_cart_service.checkout(1,mock_payment_info,mock_purchase_order)





# ## --------       DELETE SHOPPING CART     --------


def test_delete_product(monkeypatch,test_shopping_cart_service):

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    def request_get_product(url):
        return MockResponse(mock_product1, 200)

    import requests

    def side_effect(url):
        if "users" in url:
            return request_get_user(url)
        elif "products" in url:
            return request_get_product(url)
        else:
            raise ValueError("Unknown URL")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect
    )

    def mock_delete_product(user_id, product_id):
        return None
    
    
    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.delete_product = Mock(spec=mock_delete_product)

    shopping_cart_service.delete_product(1, 1)

    shopping_cart_dao_mock.delete_product.assert_called_once_with(
        user_id=1, product_id=1)

# # ## --------       EMPTY SHOPPING CART     --------

def test_empty(monkeypatch,test_shopping_cart_service):

    def request_get_user(url):
        return MockResponse(mock_user, 200)
    
    import requests

    def side_effect(url):
        if "users" in url:
            return request_get_user(url)
        else:
            raise ValueError("Unknown URL")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect
    )

    
    def mock_empty(user_id):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_service.empty(1)

    shopping_cart_dao_mock.empty.assert_called_once_with(1)
    
