import datetime


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


mock_product1 = {
    "id": 1,
    "category": {
        "id": 1,
        "name": "category",
    },
    "name": "product_name",
    "tags": ["tag1", "tag2"],
    "price": 1,
    "stock": 3,
    "owner": {
        "id": 1,
        "username": "username",
    },
    "score": 0,
}
mock_product2 = {
    "id": 2,
    "category": {
        "id": 1,
        "name": "category",
    },
    "name": "product_name",
    "tags": ["tag1", "tag2"],
    "price": 1,
    "stock": 5,
    "owner": {
        "id": 1,
        "username": "username",
    },
    "score": 0,
}

def request_get_product_200(url):
    if "products/1" in url:
        return MockResponse(mock_product1, 200)
    elif "products/2" in url:
        return MockResponse(mock_product2, 200)
    else:
        raise ValueError("Unknown Product")


