import pytest
from src.api.models.categories import Category
from unittest.mock import MagicMock


def test_get_categories(monkeypatch, test_category_dao):
    mock_categories = [Category(id=1, name="Categoria 1"), 
                       Category(id=2, name="Categoria 2")]


    category_db_model_mock = MagicMock()
    query_mock = MagicMock()
    query_mock.all = lambda: mock_categories
    category_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.category_dao_impl.Category",
        category_db_model_mock,
    )

    category_dao, db_mock = test_category_dao

    categories = category_dao.get_categories()

    assert len(categories) == len(mock_categories)
    assert categories[0].id == mock_categories[0].id
    assert categories[0].name == categories[0].name
    assert categories[1].id == mock_categories[1].id
    assert categories[1].name == categories[1].name

def test_create_category(monkeypatch, test_category_dao):

    category_db_model_mock = MagicMock()
    monkeypatch.setattr(
        "src.api.persistence.category_dao_impl.Category",
        category_db_model_mock,
    )

    category_dao, db_mock = test_category_dao

    name = "Categoria 1"
    category = category_dao.create_category(name)

    db_mock.session.add.assert_called_once()
    db_mock.session.commit.assert_called_once()



def get_category_by_id(monkeypatch, test_category_dao):
    mock_category = Category(id=1, name="Categoria 1")

    category_db_model_mock = MagicMock()
    query_mock = MagicMock()
    query_mock.get = lambda category_id: mock_category
    category_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.category_dao_impl.Category",
        category_db_model_mock,
    )

    category_dao, db_mock = test_category_dao

    category = category_dao.get_categories()

    assert category.id == mock_category.id
    assert category.name == mock_category.name

def get_category_by_id_non_existent(monkeypatch, test_category_dao):
    mock_category = None

    category_db_model_mock = MagicMock()
    query_mock = MagicMock()
    query_mock.get = lambda category_id: mock_category
    category_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.category_dao_impl.Category",
        category_db_model_mock,
    )

    category_dao, db_mock = test_category_dao

    category = category_dao.get_categories()
    assert category is None

def test_update_category(monkeypatch, test_category_dao):
    mock_category = Category(id=1, name="Categoria 1")

    category_dao, db_mock = test_category_dao

    category_dao.update_category(mock_category, "Categoria 2")
    db_mock.session.commit.assert_called_once()