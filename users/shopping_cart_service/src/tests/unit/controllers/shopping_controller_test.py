import pytest
from flask import url_for
from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.models.shopping_cart import ShoppingCarts

## --------       GET SHOPPING CART    --------

def test_get_shopping_cart_products(monkeypatch):

    def mock_get_user_by_id(user_id):
        user = User(username="test", email="test@test.com", password="12345678")
        user.id = 1
        return user if user.id = '1' else None

    def mock_get_shopping_cart_by_user_id(user_id):
        return ShoppingCarts(user_id=1, product_id=1, quantity=1)

    monkeypatch.setattr(ShoppingCartService, 'get_user_by_id', mock_get_user_by_id)
    monkeypatch.setattr(ShoppingCartService, 'get_shopping_cart_by_user_id', mock_get_shopping_cart_by_user_id)

    test_app = app.test_client()

    # Test with existing user
    response = test_app.get(url_for('shopping_cart.get_shopping_cart_products', user_id='1'))
    assert response.status_code == 200

    # Test with non-existing user
    response = test_app.get(url_for('shopping_cart.get_shopping_cart_products', user_id='2'))
    assert response.status_code == 404

## --------       GET SHOPPING CART PRODUCTS     --------

def test_get_shopping_cart_products(monkeypatch):

    def mock_get_user_by_id(user_id):
        user = User(username="test", email="test@test.com", password="12345678")
        user.id = 1
        return user if user.id = '1' else None

    def mock_get_shopping_cart_by_user_id(user_id):
        return ShoppingCarts(user_id=1, product_id=1, quantity=1)

    monkeypatch.setattr(ShoppingCartService, 'get_user_by_id', mock_get_user_by_id)
    monkeypatch.setattr(ShoppingCartService, 'get_shopping_cart_by_user_id', mock_get_shopping_cart_by_user_id)

    test_app = app.test_client()

    response = test_app.get(url_for('shopping_cart.get_shopping_cart_products', user_id='1'))
    assert response.status_code == 200

    response = test_app.get(url_for('shopping_cart.get_shopping_cart_products', user_id='2'))
    assert response.status_code == 404

## --------       DELETE SHOPPING CART    --------

def test_delete_shopping_cart(monkeypatch):

    def mock_delete_shopping_cart(user_id):
        return None

    monkeypatch.setattr(ShoppingCartService, 'delete_shopping_cart', mock_delete_shopping_cart)

    test_app = app.test_client()

    response = test_app.delete(url_for('shopping_cart.delete_shopping_cart', user_id='1'))
    assert response.status_code == 204