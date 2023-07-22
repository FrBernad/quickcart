import pytest
from src.api.models.product import Product

from src.tests.mocks import (

    request_get_user_200,
    request_get_category_200,
    mock_product1,
    mock_product2
)
from unittest.mock import MagicMock

## --------       CREATE PRODUCT     --------

def test_create_product(monkeypatch, test_product_service):

    def mock_create_product(
            user_id,
            name,
            price,
            category_id,
            tags,
            stock):
        return mock_product1
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    product_service, product_dao_mock = test_product_service

    product_dao_mock.create_product = mock_create_product

    product = product_service.create_product(mock_product1.user_id, 
                                             mock_product1.name, 
                                             mock_product1.price, 
                                             mock_product1.category_id, 
                                             mock_product1.tags, 
                                             mock_product1.stock)
    
    assert mock_product1.id == product.id
    assert mock_product1.name == product.name
    assert mock_product1.stock == product.stock
    assert mock_product1.score == product.score
    assert mock_product1.user_id == product.owner['id']
    assert mock_product1.category_id == product.category['id']

# ## --------       GET PRODUCT     --------

def test_get_products(monkeypatch, test_product_service):
    def mock_get_product():
        return [mock_product1, mock_product2]
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    product_service, product_dao_mock = test_product_service

    product_dao_mock.get_products = mock_get_product

    products = product_service.get_products()
    
    assert mock_product1.id == products[0].id
    assert mock_product1.name == products[0].name
    assert mock_product1.stock == products[0].stock
    assert mock_product1.score == products[0].score
    assert mock_product1.user_id == products[0].owner['id']
    assert mock_product1.category_id == products[0].category['id']

    assert mock_product2.id == products[1].id
    assert mock_product2.name == products[1].name
    assert mock_product2.stock == products[1].stock
    assert mock_product2.score == products[1].score
    assert mock_product2.user_id == products[1].owner['id']
    assert mock_product2.category_id == products[1].category['id']
   

# ## --------       GET PRODUCT BY ID    --------


def test_get_product_by_id(monkeypatch, test_product_service):
    def mock_get_product_by_id(product_id):
        return mock_product1
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    product_service, product_dao_mock = test_product_service

    product_dao_mock.get_product_by_id = mock_get_product_by_id

    product = product_service.get_product_by_id(1)
    
    assert mock_product1.id == product.id
    assert mock_product1.name == product.name
    assert mock_product1.stock == product.stock
    assert mock_product1.score == product.score
    assert mock_product1.user_id == product.owner['id']
    assert mock_product1.category_id == product.category['id']


# # ## --------       UPDATE PRODUCT     --------

def test_update_product(monkeypatch, test_product_service):
    def mock_update_product(product, 
                            name, 
                            price, 
                            category_id, 
                            tags):
        return None
    
    def mock_get_product_by_id(product_id):
        return mock_product1
    
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    product_service, product_dao_mock = test_product_service

    product_dao_mock.update_product = MagicMock(spec=mock_update_product)
    product_dao_mock.get_product_by_id = MagicMock(spec=mock_get_product_by_id,return_value=mock_product1)

    product = product_service.update_product(mock_product1.user_id,
                                             mock_product1.id,
                                             mock_product1.name,
                                             mock_product1.price,
                                             mock_product1.category_id,
                                             mock_product1.tags)
    

    product_dao_mock.update_product.assert_called_once_with(mock_product1,
                                                            mock_product1.name,
                                                            mock_product1.price,
                                                            mock_product1.category_id,
                                                            mock_product1.tags)


# # ## --------       DELETE PRODUCT     --------

def test_delete_product(monkeypatch, test_product_service):
    def mock_delete_product(product_id):
        return None

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    product_service, product_dao_mock = test_product_service

    product_dao_mock.delete_product = MagicMock(spec=mock_delete_product)

    product = product_service.delete_product(mock_product1.id)
    
    product_dao_mock.delete_product.assert_called_once_with(mock_product1.id)


# # # ## --------       UPDATE PRODUCT SCORE     --------

def test_update_product_score(monkeypatch, test_product_service):
    def mock_update_product_score(product,score):
        return None
    
    def mock_get_product_by_id(product_id):
        return mock_product1
    
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )
    
    product_service, product_dao_mock = test_product_service

    product_dao_mock.update_product_score = MagicMock(spec=mock_update_product_score)
    product_dao_mock.get_product_by_id = MagicMock(spec=mock_get_product_by_id,return_value=mock_product1)

    product = product_service.update_product_score(mock_product1.id,
                                             mock_product1.score)
    
    product_dao_mock.update_product_score.assert_called_once_with(mock_product1,
                                                            mock_product1.score)

# # ## --------       UPDATE PRODUCT STOCK    --------

def test_update_product_stock(monkeypatch, test_product_service):
    def mock_update_product_stock(product,stock):
        return None
    
    def mock_get_product_by_id(product_id):
        return mock_product1
    
    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )
    
    product_service, product_dao_mock = test_product_service

    product_dao_mock.update_product_stock = MagicMock(spec=mock_update_product_stock)
    product_dao_mock.get_product_by_id = MagicMock(spec=mock_get_product_by_id,return_value=mock_product1)

    product = product_service.update_product_stock(mock_product1.id,
                                             mock_product1.stock)
    

    product_dao_mock.update_product_stock.assert_called_once_with(mock_product1,
                                                            mock_product1.stock)