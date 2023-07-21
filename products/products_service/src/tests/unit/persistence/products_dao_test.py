import pytest
from src.api.models.shopping_cart_product import ShoppingCartProduct
from unittest.mock import MagicMock


def test_get_products(monkeypatch, test_shopping_cart_dao):
    mock_products = [ShoppingCartProduct(user_id=1, product_id=1, quantity=1)]

    shopping_cart_db_model_mock = MagicMock()
    query_mock = MagicMock()
    all_mock = MagicMock()
    all_mock.all = lambda: mock_products
    query_mock.filter_by = lambda user_id: all_mock
    shopping_cart_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
        shopping_cart_db_model_mock,
    )

    shopping_cart_dao, db_mock = test_shopping_cart_dao

    user_id = 1

    products = shopping_cart_dao.get_products(user_id)

    assert len(mock_products) == len(products)
    assert mock_products[0].user_id == products[0].user_id
    assert mock_products[0].product_id == products[0].product_id
    assert mock_products[0].quantity == products[0].quantity


def test_add_product(monkeypatch, test_shopping_cart_dao):
    shopping_cart_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock()
    first_mock.first = lambda: []
    query_mock.filter_by = lambda user_id, product_id: first_mock
    shopping_cart_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
        shopping_cart_db_model_mock,
    )

    shopping_cart_dao, db_mock = test_shopping_cart_dao

    user_id = 1
    product_id = 1
    quantity = 3

    shopping_cart_dao.add_product(user_id, product_id, quantity)

    db_mock.session.add.assert_called_once()
    db_mock.session.commit.assert_called_once()


def test_update_product(monkeypatch, test_shopping_cart_dao):
    mock_product = ShoppingCartProduct(user_id=1, product_id=1, quantity=1)

    shopping_cart_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock()
    first_mock.first = lambda: mock_product
    query_mock.filter_by = lambda user_id, product_id: first_mock
    shopping_cart_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
        shopping_cart_db_model_mock,
    )

    shopping_cart_dao, db_mock = test_shopping_cart_dao

    user_id = 1
    product_id = 1
    quantity = 3

    shopping_cart_dao.add_product(user_id, product_id, quantity)

    assert mock_product.user_id == user_id
    assert mock_product.product_id == product_id
    assert mock_product.quantity == quantity

    db_mock.session.commit.assert_called_once()


def test_delete_product(monkeypatch, test_shopping_cart_dao):
    shopping_cart_db_model_mock = MagicMock()
    query_mock = MagicMock()
    delete_mock = MagicMock()
    delete_mock.delete = delete_mock
    query_mock.filter_by = lambda user_id, product_id: delete_mock
    shopping_cart_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
        shopping_cart_db_model_mock,
    )

    shopping_cart_dao, db_mock = test_shopping_cart_dao

    user_id = 1
    product_id = 1

    shopping_cart_dao.delete_product(user_id, product_id)

    delete_mock.assert_called_once()
    db_mock.session.commit.assert_called_once()


def test_empty(monkeypatch, test_shopping_cart_dao):
    shopping_cart_db_model_mock = MagicMock()
    query_mock = MagicMock()
    delete_mock = MagicMock()
    delete_mock.delete = delete_mock
    query_mock.filter_by = lambda user_id: delete_mock
    shopping_cart_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.shopping_cart_dao_impl.ShoppingCartProduct",
        shopping_cart_db_model_mock,
    )

    shopping_cart_dao, db_mock = test_shopping_cart_dao

    user_id = 1

    shopping_cart_dao.empty(user_id)

    delete_mock.assert_called_once()
    db_mock.session.commit.assert_called_once()
