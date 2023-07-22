import pytest
from src.api.interfaces.exceptions.product_out_of_stock_exception import ProductOutOfStockException
from unittest.mock import MagicMock
from unittest.mock import Mock
import copy
from src.tests.mocks import (
    mock_product1,
    mock_product2,
    mock_shopping_cart_product1,
    mock_shopping_cart_product2,
    mock_payment_info,
    mock_comment,
    request_get_user_200,
    request_get_product_200,
    request_decrease_stock_product_204,
    request_create_purchase_order_200
)


## --------       GET SHOPPING CART     --------

def test_get_products(monkeypatch,test_shopping_cart_service):
    mock_products = [mock_shopping_cart_product1,
                     mock_shopping_cart_product2]

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

    def mock_get_products(user_id):
        return mock_products

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.get_products = mock_get_products

    products = shopping_cart_service.get_products(1)

    assert len(products) == len(mock_products)
    assert products[0]['product_id'] == mock_product1['id']
    assert products[1]['product_id'] == mock_product2['id']

## --------       UPDATE/ ADD SHOPPING CART     --------

def test_add_product(monkeypatch, test_shopping_cart_service):

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
    def mock_add_product(user_id, product_id, quantity):
        return None

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.add_product = MagicMock(spec=mock_add_product)

    shopping_cart_service.add_product(1, 1, 1)
    shopping_cart_dao_mock.add_product.assert_called_once_with(1,1,1)

def test_add_product_out_of_stock_exception(monkeypatch, test_shopping_cart_service):

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
    def mock_add_product(user_id, product_id, quantity):
        return None

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.add_product = MagicMock(spec=mock_add_product)

    with pytest.raises(ProductOutOfStockException):
        # Big quantity
        shopping_cart_service.add_product(1, 1, 100)
    


## --------       CHECKOUT SHOPPING CART     --------

def test_checkout(monkeypatch,test_shopping_cart_service):
    mock_products = [mock_shopping_cart_product1,
                     mock_shopping_cart_product2
                    ]

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

    def mock_empty(user_id):
        return
    
    def mock_get_products(user_id):
        return
    

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_dao_mock.get_products = MagicMock(spec=mock_get_products,return_value=mock_products)

    shopping_cart_service.checkout(1,mock_payment_info,mock_comment)
    shopping_cart_dao_mock.empty.assert_called()



def test_checkout_product_out_of_stock_exception(monkeypatch,test_shopping_cart_service):
    mock_shopping_cart_product2_with_huge_quantity = copy.deepcopy(mock_shopping_cart_product2)
    mock_shopping_cart_product2_with_huge_quantity.quantity = 90

    mock_products = [mock_shopping_cart_product1,
                     mock_shopping_cart_product2_with_huge_quantity
                    ]
  
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

    def mock_empty(user_id):
        return
    
    def mock_get_products(user_id):
        return
    
    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_dao_mock.get_products = MagicMock(spec=mock_get_products,return_value=mock_products)

    with pytest.raises(ProductOutOfStockException):
        shopping_cart_service.checkout(1,mock_payment_info,mock_comment)


# ## --------       DELETE SHOPPING CART     --------


def test_delete_product(monkeypatch,test_shopping_cart_service):

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

    def mock_delete_product(user_id, product_id):
        return None
    
    
    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.delete_product = Mock(spec=mock_delete_product)

    shopping_cart_service.delete_product(1, 1)

    shopping_cart_dao_mock.delete_product.assert_called_once_with(
        user_id=1, product_id=1)

# # ## --------       EMPTY SHOPPING CART     --------

def test_empty(monkeypatch,test_shopping_cart_service):
    
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

    
    def mock_empty(user_id):
        return

    shopping_cart_service, shopping_cart_dao_mock = test_shopping_cart_service

    shopping_cart_dao_mock.empty = MagicMock(spec=mock_empty)

    shopping_cart_service.empty(1)

    shopping_cart_dao_mock.empty.assert_called_once_with(1)
    
