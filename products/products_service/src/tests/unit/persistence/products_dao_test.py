import pytest
from src.api.models.product import Product
from unittest.mock import MagicMock



# def test_create_product(monkeypatch, test_product_dao):
#     mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1)]

#     shopping_cart_db_model_mock = MagicMock()
#     query_mock = MagicMock()
#     all_mock = MagicMock()
#     all_mock.all = lambda: mock_products
#     query_mock.filter_by = lambda user_id: all_mock
#     shopping_cart_db_model_mock.query = query_mock
#     monkeypatch.setattr(
#         "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
#         shopping_cart_db_model_mock,
#     )

#     shopping_cart_dao, db_mock = test_shopping_cart_dao

#     user_id = 1

#     products = shopping_cart_dao.get_products(user_id)

#     assert len(mock_products) == len(products)
#     assert mock_products[0].user_id == products[0].user_id
#     assert mock_products[0].product_id == products[0].product_id
#     assert mock_products[0].quantity == products[0].quantity


# def test_delete_product(monkeypatch, test_product_dao):

   

# def get_products(monkeypatch, test_product_dao):





# def get_product_by_id(monkeypatch, test_product_dao):


# def update_product(monkeypatch, test_product_dao):


# def update_product_score(monkeypatch, test_product_dao):

# def update_product_stock(monkeypatch, test_product_dao):

# def _get_and_generate_tags(monkeypatch, test_product_dao):
       