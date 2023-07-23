import pytest
from src.api.services.shopping_cart_service_impl import ShoppingCartServiceImpl
from src.api.models.shopping_cart_product import ShoppingCartProduct
from src.api.interfaces.exceptions.user_not_found_exception import UserNotFoundException
from src.api.interfaces.exceptions.service_unavailable_exception import ServiceUnavailableException
from src.api.interfaces.exceptions.bad_request_exception import BadRequestException
from src.api.interfaces.exceptions.not_found_exception import NotFoundException
from src.api.interfaces.exceptions.product_not_found_exception import ProductNotFoundException
from src.api.interfaces.exceptions.product_out_of_stock_exception import ProductOutOfStockException
from src.api.interfaces.exceptions.service_internal_exception import ServiceInternalException
import json

## --------       GET SHOPPING CART     --------

def test_get_shopping_cart_products(test_client, monkeypatch):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1)]

    def mock_get_products(self, user_id):
        return mock_products

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(mock_products) == len(data)
    assert mock_products[0].product_id == data[0]["product_id"]
    assert mock_products[0].quantity == data[0]["quantity"]

def test_get_shopping_cart_products_empty(test_client, monkeypatch):
    mock_products = []

    def mock_get_products(self, user_id):
        return mock_products

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 204



def test_get_shopping_cart_products_invalid_user_id(test_client, monkeypatch):

    def mock_get_products(self, user_id):
        raise UserNotFoundException(user_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 404

def test_get_shopping_cart_products_user_service_internal_error(test_client, monkeypatch):

    def mock_get_products(self, user_id):
        raise ServiceInternalException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 500


def test_get_shopping_cart_products_user_service_unavailable_error(test_client, monkeypatch):

    def mock_get_products(self, user_id):
        raise ServiceUnavailableException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 500

def test_get_shopping_cart_products_invalid_product_id(test_client, monkeypatch):

    mock_product_id = 1
    def mock_get_products(self, user_id):
        raise ProductNotFoundException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 404

def test_get_shopping_cart_products_product_service_internal_error(test_client, monkeypatch):

    def mock_get_products(self, user_id):
        raise ServiceInternalException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 500


def test_get_shopping_cart_products_product_service_unavailable_error(test_client, monkeypatch):

    def mock_get_products(self, user_id):
        raise ServiceUnavailableException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1"
    )

    assert resp.status_code == 500

## --------       UPDATE SHOPPING CART     --------


def test_update_shopping_cart_product_quantity(test_client, monkeypatch):
    def mock_add_product(self, user_id, product_id, quantity):
        return None

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 204


def test_update_shopping_cart_product_with_invalid_quantity(test_client, monkeypatch):
    def mock_add_product(self, user_id, product_id, quantity):
        return None

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": -1,
            }
        ),
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_update_shopping_cart_product_missing_quantity(test_client, monkeypatch):
    def mock_add_product(self, user_id, product_id, quantity):
        return None

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
            }
        ),
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_update_shopping_cart_product_invalid_user_id(test_client, monkeypatch):

    def mock_add_product(self, user_id, product_id, quantity):
        raise UserNotFoundException(user_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)


 
    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 404

def test_update_shopping_cart_product_user_service_internal_error(test_client, monkeypatch):

    def mock_add_product(self, user_id, product_id, quantity):
        raise ServiceInternalException("user")


    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)



    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 500


def test_update_shopping_cart_product_user_service_unavailable_error(test_client, monkeypatch):

    def mock_add_product(self, user_id, product_id, quantity):
        raise ServiceUnavailableException("user")


    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )
    assert resp.status_code == 500

def test_update_shopping_cart_product_invalid_product_id(test_client, monkeypatch):

    mock_product_id = 1

    def mock_add_product(self, user_id, product_id, quantity):
        raise ProductNotFoundException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 404

def test_update_shopping_cart_product_product_service_internal_error(test_client, monkeypatch):


    def mock_add_product(self, user_id, product_id, quantity):
        raise ServiceInternalException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 500


def test_update_shopping_cart_product_service_unavailable_error(test_client, monkeypatch):

    def mock_add_product(self, user_id, product_id, quantity):
        raise ServiceUnavailableException("products")
    
    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )
    assert resp.status_code == 500


def test_update_shopping_cart_product_out_of_stock(test_client, monkeypatch):

    mock_product_id = 1
    def mock_add_product(self, user_id, product_id, quantity):
        raise ProductOutOfStockException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "add_product", mock_add_product)

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 2,
            }
        ),
    )

    assert resp.status_code == 400

## --------       CHECKOUT SHOPPING CART     --------

def test_checkout_shopping_cart(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        return None

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 204

def test_checkout_shopping_cart_invalid_user_id(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        raise UserNotFoundException(user_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 404

def test_checkout_shopping_cart_user_service_unavailable_error(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        raise ServiceUnavailableException("users")

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 500

def test_checkout_shopping_cart_user_service_internal_error(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        raise ServiceInternalException("users")

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 500

def test_checkout_shopping_cart_invalid_product_id(test_client, monkeypatch):
    mock_product_id = 1
    def mock_checkout(self, user_id, payment_info,comments):
        raise ProductNotFoundException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 404

def test_checkout_shopping_cart_product_service_unavailable_error(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        raise ServiceUnavailableException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 500

def test_checkout_shopping_cart_product_service_internal_error(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        raise ServiceInternalException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 500

def test_checkout_shopping_cart_product_out_of_stock(test_client, monkeypatch):
    mock_product_id = 1 
    def mock_checkout(self, user_id, payment_info,comments):
        raise ProductOutOfStockException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 400


def test_checkout_shopping_cart_with_invalid_information(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARD",
                "card_number": "1234 1234 1234 1234",
                "expiration_month": 11,
                "cvv": 123,
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]
def test_checkout_shopping_cart_missing_information(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info,comments):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "checkout", mock_checkout)

    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
              
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


# ## --------       DELETE SHOPPING CART     --------


def test_delete_shopping_cart_product(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 204


def test_delete_shopping_cart_product_invalid_user_id(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        raise UserNotFoundException(user_id)


    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 404


def test_delete_shopping_cart_product_user_service_internal_error(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        raise ServiceInternalException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 500

def test_delete_shopping_cart_product_user_service_unavailable_error(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        raise ServiceUnavailableException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 500

def test_delete_shopping_cart_product_invalid_product_id(test_client, monkeypatch):
    mock_product_id = 1
    def mock_delete_product(self, user_id, product_id):
        raise ProductNotFoundException(mock_product_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 404

def test_delete_shopping_cart_product_service_internal_error(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        raise ServiceInternalException("products")

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 500

def test_delete_shopping_cart_product_product_service_unavailable_error(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        raise ServiceUnavailableException("products")
    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )
    assert resp.status_code == 500


# # ## --------       EMPTY SHOPPING CART     --------


def test_empty_shopping_cart(test_client, monkeypatch):
    def mock_empty(self, user_id):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "empty", mock_empty)

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 204


def test_empty_shopping_cart_invalid_user_id(test_client, monkeypatch):
    def mock_empty(self, user_id):
        raise UserNotFoundException(user_id)

    monkeypatch.setattr(ShoppingCartServiceImpl, "empty", mock_empty)

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 404


def test_empty_shopping_cart_user_service_internal_error(test_client, monkeypatch):
    def mock_empty(self, user_id):
        raise ServiceInternalException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "empty", mock_empty)

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 500

def test_empty_shopping_cart_user_service_unavailable_error(test_client, monkeypatch):
    def mock_empty(self, user_id):
        raise ServiceUnavailableException("user")

    monkeypatch.setattr(ShoppingCartServiceImpl, "empty", mock_empty)

    resp = test_client.delete(
        "/shopping-cart/1",
    )


    assert resp.status_code == 500
