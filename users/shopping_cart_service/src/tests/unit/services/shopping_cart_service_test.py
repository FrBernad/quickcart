import pytest
from src.api.persistence.shopping_cart_dao_impl import ShoppingCartDaoImpl
from src.api.models.shopping_cart_product import ShoppingCartProduct
from src.api.services.shopping_cart_service_impl import ShoppingCartService
from unittest.mock import MagicMock


def test_get_products(test_shopping_cart_service):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1)]

    def mock_get_products(user_id):
        return mock_products

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.get_products = mock_get_products

    products = shopping_cart_service.get_products(1)

    assert len(products) == len(mock_products)
    assert products[0].user_id == mock_products[0].user_id
    assert products[0].product_id == mock_products[0].product_id
    assert products[0].quantity == mock_products[0].quantity


def test_add_product(test_shopping_cart_service):
    def mock_add_product(user_id, product_id, quantity):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.add_product = MagicMock(spec=mock_add_product)

    shopping_cart_service.add_product(1, 1, 1)

    shopping_cart_dao_mock.add_product.assert_called()


def test_checkout(test_shopping_cart_service):
    def mock_empty(user_id):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_service.empty(1)

    shopping_cart_dao_mock.empty.assert_called()


def test_delete_product(test_shopping_cart_service):
    def mock_delete_product(user_id, product_id):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.delete_product = MagicMock(spec=mock_delete_product)

    shopping_cart_service.delete_product(1, 1)

    shopping_cart_dao_mock.delete_product.assert_called()


def test_empty(test_shopping_cart_service):
    def mock_empty(user_id):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_service.empty(1)

    shopping_cart_dao_mock.empty.assert_called()
