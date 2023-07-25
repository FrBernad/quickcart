import pytest
from src.api.models.product import Product
from src.api.models.tag import Tag
from unittest.mock import MagicMock


def test_create_product(monkeypatch, test_product_dao):
    product_db_model_mock = MagicMock()
    all_mock = MagicMock()
    all_mock.all = lambda: []
    
    product_dao, db_mock = test_product_dao

    monkeypatch.setattr(
        "src.api.persistence.product_dao_impl.Product",
        product_db_model_mock,
    )

    def mock_scalars(*args, **kwargs):
        return all_mock

    # Patch the actual database query with the mock implementation
    monkeypatch.setattr(product_dao.db.session, 'scalars', mock_scalars)

    user_id = 1
    name = "iPhone"
    price = 1200.5
    category_id = 1
    tags = ['black']
    stock = 5

    product_dao.create_product(user_id, name, price, category_id, tags, stock)

    db_mock.session.add.assert_called_once()
    db_mock.session.commit.assert_called_once()

def test_create_product_existing_tag(monkeypatch, test_product_dao):
    product_db_model_mock = MagicMock()
    all_mock = MagicMock()
    all_mock.all = lambda: [Tag(id=1, name='black')]
    
    product_dao, db_mock = test_product_dao

    monkeypatch.setattr(
        "src.api.persistence.product_dao_impl.Product",
        product_db_model_mock,
    )

    def mock_scalars(*args, **kwargs):
        return all_mock

    monkeypatch.setattr(product_dao.db.session, 'scalars', mock_scalars)

    user_id = 1
    name = "iPhone"
    price = 1200.5
    category_id = 1
    tags = ['black']
    stock = 5

    product_dao.create_product(user_id, name, price, category_id, tags, stock)

    db_mock.session.add.assert_called_once()
    db_mock.session.commit.assert_called_once()