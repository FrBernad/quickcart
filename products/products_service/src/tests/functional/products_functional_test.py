from src.api.models.product import Product
from src.api.models.tag import Tag
from src.api.services.product_service_impl import ProductServiceImpl
from src.tests.mocks import (
    mock_product_map1,
    mock_product_map2,
    mock_product_map_post,
    mock_product_map_put,
    request_get_user_200,
    request_get_category_200,
)
import json

## --------       CREATE PRODUCT     --------
# def test_create_product(monkeypatch,test_client, test_database):
#     def mock_create_product(self,user_id, name, price, category_id, tags, stock):
#         return mock_product_map1

#     monkeypatch.setattr(ProductServiceImpl, "create_product", mock_create_product)

#     resp = test_client.post(
#         "/products",
#         data=json.dumps(
#             mock_product_map_post
#         ),
#         content_type="application/json",
#     )

#     data = json.loads(resp.data)
#     assert resp.status_code == 201
#     assert data['id'] == mock_product_map_post['id']
#     assert data['name'] == mock_product_map_post['name']
#     assert data['category']['id'] == mock_product_map_post['category_id']
#     assert data['stock'] == mock_product_map_post['stock']
#     assert data['owner']['id'] == mock_product_map_post['user_id']
#     assert data['tags'][0]['name'] == mock_product_map_post['tags'][0]
#     assert data['tags'][1]['name'] == mock_product_map_post['tags'][1]


# --------       GET PRODUCT BY ID    --------

def test_get_product_by_id(monkeypatch, test_client, test_database):
    mock_tag1 = Tag(id=1,name="Tag 1")
    mock_tag2 = Tag(id=2,name="Tag 2")

    mock_product1 = Product(id = 1, user_id = 1, category_id = 1, name = "Producto 1", \
                            stock = 4, price = 120.0, score = 0.0, tags = [mock_tag1, mock_tag2])

    product1 = mock_product1
    product_id = product1.id
    tag1 = mock_tag1
    test_database.session.add(tag1)
    test_database.session.add(product1)
    test_database.session.commit()

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(requests, "get", side_effect_get)

    resp = test_client.get(
        f"/products/{product_id}",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert data['id'] == product1.id

def test_get_product_by_id_not_found(monkeypatch, test_client, test_database):

    resp = test_client.get(
        f"/products/1",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 404

## --------       GET PRODUCTS    --------

def test_get_products(monkeypatch, test_client, test_database):
    mock_tag1 = Tag(id=1,name="Tag 1")
    mock_tag2 = Tag(id=2,name="Tag 2")

    mock_product1 = Product(id = 1, user_id = 1, category_id = 1, name = "Producto 1", \
                            stock = 4, price = 120.0, score = 0.0, tags = [mock_tag1, mock_tag2])

    mock_product2 = Product(id = 2, user_id = 1, category_id = 1, name = "Producto 2", \
                            stock = 4, price = 120.0, score = 0.0, tags = [])

    tag1 = mock_tag1
    tag2 = mock_tag2
    test_database.session.add(tag1)
    test_database.session.add(tag2)
    product1 = mock_product1
    product2 = mock_product2
    test_database.session.add(product1)
    test_database.session.add(product2)
    test_database.session.commit()
    products = [product1, product2]

    import requests

    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "categories" in url:
            return request_get_category_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(requests, "get", side_effect_get)

    resp = test_client.get(
        "/products",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == len(products)



# ## --------       UPDATE PRODUCT     --------

# def test_update_product(monkeypatch,test_client, test_database):


# ## --------       DELETE PRODUCT     --------

# def test_delete_product(monkeypatch,test_client, test_database ):


# ## --------       UPDATE PRODUCT SCORE     --------

# def test_update_product_score(monkeypatch,test_client, test_database):


# ## --------       UPDATE PRODUCT STOCK    --------


# def test_update_product_stock(monkeypatch,test_client, test_database):
