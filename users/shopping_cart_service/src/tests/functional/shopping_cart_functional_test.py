import pytest
from src.api.models.shopping_cart_product import ShoppingCartProduct
from src.tests.mocks import (
    mock_shopping_cart_product1,
    mock_shopping_cart_product2,
    request_get_user_200,
    request_get_product_200,
    request_get_product_404,
    request_get_user_404,
    request_decrease_stock_product_204,
    request_create_purchase_order_200
)
import json

## --------       GET SHOPPING CART     --------


def test_get_shopping_cart_products(monkeypatch,test_client, test_database):
    product = mock_shopping_cart_product1
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    resp = test_client.get(
        "/shopping-cart/1",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == 1
    assert product.product_id == data[0]["product_id"]
    assert product.quantity == data[0]["quantity"]

## --------       UPDATE/ ADD SHOPPING CART     --------


def test_update_shopping_cart_product_quantity(monkeypatch,test_client, test_database):
    product = mock_shopping_cart_product1
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

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

def test_update_shopping_cart_product_quantity_out_of_stock(monkeypatch,test_client, test_database):
    product = mock_shopping_cart_product1
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": 90,
            }
        ),
    )

    assert resp.status_code == 400


def test_update_shopping_cart_product_with_invalid_quantity(test_client, test_database):
    
    resp = test_client.put(
        "/shopping-cart/1/1",
        content_type="application/json",
        data=json.dumps(
            {
                "quantity": -2,
            }
        ),
    )

    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]

def test_update_shopping_cart_product_missing_quantity(test_client, test_database):
    
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

def test_update_shopping_cart_product_quantity_invalid_product_id(monkeypatch,test_client, test_database):
    product = mock_shopping_cart_product1
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_404(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

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

def test_update_shopping_cart_product_quantity_invalid_user_id(monkeypatch,test_client, test_database):
    product = mock_shopping_cart_product1
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_404(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

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


## --------       CHECKOUT SHOPPING CART     --------

def test_checkout_shopping_cart(monkeypatch,test_client, test_database):
    product1 = mock_shopping_cart_product1
    test_database.session.add(product1)
    test_database.session.commit()
    product2 = mock_shopping_cart_product2
    test_database.session.add(product2)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")
        
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    def side_effect_put(url,json):
        if "stock" in url:
            return request_decrease_stock_product_204(url,json)
        else:
            raise ValueError("Unknown URL in put method")

    monkeypatch.setattr(
        requests,
        "put",
        side_effect_put
    )
 
    def side_effect_post(url,json):
        if "purchase-orders" in url:
            return request_create_purchase_order_200(url,json)
        else:
            raise ValueError("Unknown URL in post method")
    monkeypatch.setattr(
        requests,
        "post",
        side_effect_post
    )


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


# ## --------       DELETE SHOPPING CART     --------

def test_delete_shopping_cart_product(monkeypatch,test_client, test_database):
    product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)
    test_database.session.add(product)
    test_database.session.commit()

    import requests

    def side_effect(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect
    )

    resp = test_client.delete(
        "/shopping-cart/1/1",
    )

    assert resp.status_code == 204


# # ## --------       EMPTY SHOPPING CART     --------


def test_empty_shopping(monkeypatch,test_client, test_database):

    import requests

    def side_effect(url):
        if "users" in url:
            return request_get_user_200(url)
        else:
            raise ValueError("Unknown URL")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect
    )

    resp = test_client.delete(
        "/shopping-cart/1",
    )

    assert resp.status_code == 204
