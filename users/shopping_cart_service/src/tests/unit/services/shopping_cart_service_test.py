import pytest
import json
from src.api.persistence.shopping_cart_dao_impl import ShoppingCartDaoImpl
from src.api.models.shopping_cart import ShoppingCartsDao
from src.api.models.users import User
from src.api.services.shopping_cart_service_impl import ShoppingCartService
import copy

def test_get_shopping_cart_by_user_id(test_shopping_service):
     mock_user = User(username="test", email="test@test.com", password="12345678")
     mock_user.id = 1
     mock_cart = ShoppingCarts(user_id=1, product_id=1, quantity=1)

     def mock_get_shopping_cart_by_user_id(user_id):
          return mock_cart

     shopping_cart_service, shopping_cart_dao_mock = test_shopping_service
     shopping_cart_dao_mock.get_shopping_cart_by_user_id = mock_get_shopping_cart_by_user_id
     shopping_cart = shopping_cart_service.get_shopping_cart_by_user_id(mock_user.id)

     assert shopping_cart.product_id == mock_cart.product_id
     assert shopping_cart.quantity == mock_cart.quantity
     assert shopping_cart.user_id == mock_cart.user_id


# def test_get_shopping_cart_products():

# def test_delete_shopping_cart():

# def test_add__shopping_cart_product():
     
# def test_delete_product_from_shopping_cart():

# def delete_shopping_cart(self, user_id):
