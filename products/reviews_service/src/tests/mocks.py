
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

mock_product1 = {
        "id": 1,
        "category": {
            "id": 1,
            "name": "category",
        },
        "name": "product_name",
        "tags": [
            "tag1","tag2"
        ],
        "price": 1,
        "stock": 3,
        "owner": {
            "id": 1,
            "username": "username",
        },
        "score": 0,
    }


def request_get_purchase_order_200(url):
    return MockResponse([], 200)

def request_get_user_200(url):
    return MockResponse(mock_user, 200)

def request_get_product_200(url):
    return MockResponse(mock_product1, 200)


def request_update_product_score_204(url,json):
    return MockResponse("", 204)
