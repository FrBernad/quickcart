import pytest
from flask import url_for
from src.api.services.shopping_cart_service_impl import ShoppingCartServiceImpl
from src.api.models.shopping_cart_product import ShoppingCartProduct
import json


def test_get_shopping_cart_products(test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

    resp = test_client.get(
        "/shopping-cart/1",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == 1
    assert product.product_id == data[0]["product_id"]
    assert product.quantity == data[0]["quantity"]


def test_update_shopping_cart_product_quantity(test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

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


def test_update_shopping_cart_product_with_invalid_quantity(test_client, test_database):
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


def test_checkout_shopping_cart(test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

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


def test_checkout_shopping_cart_with_invalid_information(test_client, test_database):
    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARDDD",
                "card_number": "1234123412341234",
                "expiration_year": 2023,
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_checkout_shopping_cart_with_missing_fields(test_client, test_database):
    resp = test_client.post(
        "/shopping-cart/1/checkout",
        data=json.dumps(
            {
                "payment_method": "CREDIT_CARDDD",
                "card_number": "1234123412341234",
                "expiration_month": 11,
                "cvv": "123",
                "card_type": "VISA",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_delete_shopping_cart_product(test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 204


def test_empty_shopping(test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 204
