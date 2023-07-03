import pytest
from flask import url_for
from src.api.services.shopping_cart_service_impl import ShoppingCartServiceImpl
from src.api.models.shopping_cart_product import ShoppingCartProduct
import json


def test_get_shopping_cart_products(test_client, monkeypatch):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1)]

    def mock_get_products(self, user_id):
        return mock_products

    monkeypatch.setattr(ShoppingCartServiceImpl, "get_products", mock_get_products)

    resp = test_client.get(
        "/shopping-cart/1",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(mock_products) == len(data)
    assert mock_products[0].product_id == data[0]["product_id"]
    assert mock_products[0].quantity == data[0]["quantity"]


def test_update_shopping_cart_product_quantity(test_client, monkeypatch):
    def mock_add_product(self, user_id, product_id, quantity):
        return

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
        return

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


def test_checkout_shopping_cart(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info):
        return

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

    assert resp.status_code == 200


def test_checkout_shopping_cart_with_invalid_information(test_client, monkeypatch):
    def mock_checkout(self, user_id, payment_info):
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


def test_delete_shopping_cart_product(test_client, monkeypatch):
    def mock_delete_product(self, user_id, product_id):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "delete_product", mock_delete_product)

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 204


def test_empty_shopping(test_client, monkeypatch):
    def mock_empty(self, user_id):
        return

    monkeypatch.setattr(ShoppingCartServiceImpl, "empty", mock_empty)

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 204
