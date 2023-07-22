from src.api.services.product_service_impl import ProductServiceImpl
from src.tests.mocks import (
    mock_product_map1,
    mock_product_map2,
    mock_product_map_post,
    mock_product_map_put,
    request_get_user_200,
    request_get_category_200,
    mock_tag1,
    mock_tag2,
    mock_product1,
    mock_product2

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



## --------       GET PRODUCTS    --------

def test_get_products(monkeypatch,test_client, test_database):
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

    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    resp = test_client.get(
        "/products",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == len(products)


# --------       GET PRODUCT BY ID    --------

# def test_get_product_by_id(monkeypatch,test_client, test_database):



# ## --------       UPDATE PRODUCT     --------

# def test_update_product(monkeypatch,test_client, test_database):



# ## --------       DELETE PRODUCT     --------

# def test_delete_product(monkeypatch,test_client, test_database ):


# ## --------       UPDATE PRODUCT SCORE     --------

# def test_update_product_score(monkeypatch,test_client, test_database):



# ## --------       UPDATE PRODUCT STOCK    --------


# def test_update_product_stock(monkeypatch,test_client, test_database):
