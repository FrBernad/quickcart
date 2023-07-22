from src.api.models.product import Product
from src.api.models.tag import Tag


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

mock_user = {
        "id": 1,
        "email": "string",
        "username": "string",
}

mock_product_map1 = {
    "id" : 1,
    "category" : {
        "id": 1,
        "name": "Categoria 1"
    },
    "name" : "Producto 1",
    "stock" : 4,
    "price" : 120.0,
    "score" : 0.0,
    "tags" : [
        {"id":1,
         "name":"Tag 1",
         },
         {"id":2,
         "name":"Tag 2",
         }
    ],
    "owner" : {
        "id": 1,
        "name": "Owner 1"
    },
}
mock_tag1 = Tag(id=1,name="Tag 1")
mock_tag2 = Tag(id=2,name="Tag 2")

mock_product1 = Product(
    id = 1,
    user_id = 1,
    category_id = 1,
    name = "Producto 1",
    stock = 4,
    price = 120.0,
    score = 0.0,
    tags = [
        mock_tag1,
        mock_tag2
        ]
)

mock_product_map2 = {
    "id" : 2,
    "category" : {
        "id": 1,
        "name": "Categoria 2"
    },
    "name" : "Producto 2",
    "stock" : 2,
    "price" : 120.0,
    "score" : "0",
    "tags" : [
        {"id":2,
         "name":"Tag 1",
         },
         {"id":3,
         "name":"Tag 2",
         }
    ],
    "owner" : {
        "id": 1,
        "name": "Owner 1"
    },
}
mock_product2 = Product(
    id = 2,
    user_id = 1,
    category_id = 1,
    name = "Producto 2",
    stock = 4,
    price = 120.0,
    score = 0.0,
    tags = [

        ]
)

mock_product_map_post = {
    "id" : 1,
    "user_id" : 1,
    "category_id" :1,
    "name" : "Producto 1",
    "stock" : 4,
    "price" : 120.0,
    "score" : "0",
    "tags" : [
         "Tag 1",
         "Tag 2"
         ],
}

mock_product_map_put= {
    "user_id" : 1,
    "category_id" :1,
    "name" : "Producto 1",
    "price" : 120.0,
    "tags" : [
         "Tag 1",
         "Tag 2"
    ]
}

mock_category = {
    'id': 1,
    "name": "Categoria 1"
}

def request_get_user_200(url):
    return MockResponse(mock_user, 200)

def request_get_category_200(url):
    return MockResponse(mock_category, 200)