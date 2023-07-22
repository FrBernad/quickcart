
from src.api.services.product_service_impl import ProductServiceImpl
from src.tests.mocks import (
    mock_product_map1,
    mock_product_map2,
    mock_product_map_post,
    mock_product_map_put
)
import json

## --------       CREATE PRODUCT     --------
def test_create_product(test_client,monkeypatch):
    def mock_create_product(self,user_id, name, price, category_id, tags, stock):
        return mock_product_map1

    monkeypatch.setattr(ProductServiceImpl, "create_product", mock_create_product)
    
    resp = test_client.post(
        "/products",
        data=json.dumps(
            mock_product_map_post
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 201
    assert data['id'] == mock_product_map_post['id']
    assert data['name'] == mock_product_map_post['name']
    assert data['category']['id'] == mock_product_map_post['category_id']
    assert data['stock'] == mock_product_map_post['stock']
    assert data['owner']['id'] == mock_product_map_post['user_id']
    assert data['tags'][0]['name'] == mock_product_map_post['tags'][0]
    assert data['tags'][1]['name'] == mock_product_map_post['tags'][1]



## --------       GET PRODUCTS    --------

def test_get_products(test_client,monkeypatch):
    products = [mock_product_map1,mock_product_map2]

    def mock_get_products(self):
        return products

    monkeypatch.setattr(ProductServiceImpl, "get_products", mock_get_products)
    
    resp = test_client.get(
        "/products",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == len(products)

    assert data[0]['id'] == mock_product_map1['id']
    assert data[0]['name'] == mock_product_map1['name']
    assert data[0]['category']['id'] == mock_product_map1['category']['id']
    assert data[0]['stock'] == mock_product_map1['stock']
    assert data[0]['owner']['id'] == mock_product_map1['owner']['id']
    assert data[0]['tags'][0]['name'] == mock_product_map1['tags'][0]['name']
    assert data[0]['tags'][1]['name'] == mock_product_map1['tags'][1]['name']
    assert data[1]['id'] == mock_product_map2['id']
    assert data[1]['name'] == mock_product_map2['name']
    assert data[1]['category']['id'] == mock_product_map2['category']['id']
    assert data[1]['stock'] == mock_product_map2['stock']
    assert data[1]['owner']['id'] == mock_product_map2['owner']['id']
    assert data[1]['tags'][0]['name'] == mock_product_map2['tags'][0]['name']
    assert data[1]['tags'][1]['name'] == mock_product_map2['tags'][1]['name']



## --------       GET PRODUCT BY ID    --------

def test_get_product_by_id( test_client,monkeypatch):
    product = mock_product_map1

    def mock_get_product_by_id(self,product_id):
        return product

    monkeypatch.setattr(ProductServiceImpl, "get_product_by_id", mock_get_product_by_id)
    
    resp = test_client.get(
        "/products/1",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200

    assert data['id'] == mock_product_map1['id']
    assert data['name'] == mock_product_map1['name']
    assert data['category']['id'] == mock_product_map1['category']['id']
    assert data['stock'] == mock_product_map1['stock']
    assert data['owner']['id'] == mock_product_map1['owner']['id']
    assert data['tags'][0]['name'] == mock_product_map1['tags'][0]['name']
    assert data['tags'][1]['name'] == mock_product_map1['tags'][1]['name']



## --------       UPDATE PRODUCT     --------

def test_update_product( test_client,monkeypatch):

    def mock_update_product(self,user_id,product_id, name, price, category_id, tags):
        return None

    monkeypatch.setattr(ProductServiceImpl, "update_product", mock_update_product)
    
    resp = test_client.put(
        "/products/1",
        data=json.dumps(
            mock_product_map_put
        ),
        content_type="application/json",

    )

    assert resp.status_code == 204


## --------       DELETE PRODUCT     --------

def test_delete_product(test_client, monkeypatch ):

    def mock_delete_product(self,product_id):
        return None

    monkeypatch.setattr(ProductServiceImpl, "delete_product", mock_delete_product)
    
    resp = test_client.delete(
        "/products/1"
    )

    assert resp.status_code == 204

## --------       UPDATE PRODUCT SCORE     --------

def test_update_product_score( test_client,monkeypatch):

    def mock_update_product_score(self,product_id,score):
        return None

    monkeypatch.setattr(ProductServiceImpl, "update_product_score", mock_update_product_score)
    

    resp = test_client.put(
        "/products/1/score",
        data=json.dumps({
            "score":3
        }),
        content_type="application/json",
    )

    assert resp.status_code == 204


## --------       UPDATE PRODUCT STOCK    --------


def test_update_product_stock(test_client,monkeypatch):
    def mock_update_product_stock(self,product_id,score):
        return None

    monkeypatch.setattr(ProductServiceImpl, "update_product_stock", mock_update_product_stock)
    

    resp = test_client.put(
        "/products/1/stock",
        data=json.dumps({
            "stock":3
        }),
        content_type="application/json",
    )

    assert resp.status_code == 204