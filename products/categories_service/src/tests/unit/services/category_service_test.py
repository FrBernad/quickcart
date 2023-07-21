import pytest
from src.api.models.categories import Category
from src.api.interfaces.exceptions.category_not_found_exception import CategoryNotFoundException
from unittest.mock import MagicMock


def test_get_categories(test_category_service):
    mock_categories = [Category(id=1, name="Categoria 1"), Category(id=2, name="Categoria 2")]

    def mock_get_categories():
        return mock_categories

    category_service, category_dao_mock = test_category_service

    category_dao_mock.get_categories = mock_get_categories

    categories = category_service.get_categories()

    assert len(categories) == len(mock_categories)
    assert categories[0].id == mock_categories[0].id
    assert categories[0].name == mock_categories[0].name
    assert categories[1].id == mock_categories[1].id
    assert categories[1].name == mock_categories[1].name


def test_get_category_by_id(test_category_service):
    mock_category = Category(id=1, name="Categoria 1")

    def mock_get_category_by_id(category_id):
        return mock_category


    category_service, category_dao_mock = test_category_service

    category_dao_mock.get_category_by_id = mock_get_category_by_id

    category = category_service.get_category_by_id(1)
    assert category.id == mock_category.id
    assert category.name == mock_category.name



def test_get_category_by_id_non_existent(test_category_service):

    def mock_get_category_by_id(category_id):
        return None
    
    category_service, category_dao_mock = test_category_service

    category_dao_mock.get_category_by_id = mock_get_category_by_id

    with pytest.raises(CategoryNotFoundException):
        category = category_service.get_category_by_id(1)


def test_create_category(test_category_service):
    mock_category = Category(id=1, name="Categoria 1")

    def mock_create_category(name):
        return mock_category

    category_service, category_dao_mock = test_category_service

    category_dao_mock.create_category = mock_create_category

    category = category_service.create_category("Categoria 1")

    assert category.id == mock_category.id
    assert category.name == mock_category.name


def test_update_category(test_category_service):
    mock_category = Category(id=1, name="Categoria 1")
    mock_category_updated = Category(id=1, name="Categoria 2")


    def mock_update_category(category_id,name):
        return mock_category_updated
    
    def mock_get_category_by_id(category_id):
        return mock_category
    
   
    category_service, category_dao_mock = test_category_service

    category_dao_mock.get_category_by_id = mock_get_category_by_id

    category_dao_mock.update_category = mock_update_category

    category = category_service.update_category(1,"Categoria 2")
    
    assert category.id == mock_category_updated.id
    assert category.name == mock_category_updated.name
    

def test_update_category_invalid_id(test_category_service):



    def mock_update_category(category_id,name):
        return None
    
    def mock_get_category_by_id(category_id):
        return None
    
    
    category_service, category_dao_mock = test_category_service

    category_dao_mock.get_category_by_id = mock_get_category_by_id

    category_dao_mock.update_category = mock_update_category

    with pytest.raises(CategoryNotFoundException):
        category = category_service.update_category(1,"Categoria 1")