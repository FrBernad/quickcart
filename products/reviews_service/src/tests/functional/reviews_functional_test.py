import pytest
from src.api.models.reviews import Review
from src.tests.mocks import (
    request_get_user_200,
    request_get_product_200,
    request_get_purchase_order_200,
    request_update_product_score_204,
)
import json


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def test_get_reviews_by_product(test_client, test_database):
    review = Review(product_id=1, user_id=1, review_body='test', score=4)
    test_database.session.add(review)
    test_database.session.commit()

    resp = test_client.get(
        "/reviews?product-id=1",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == 1
    assert review.product_id == data[0]["product_id"]
    assert review.user_id == data[0]["user_id"]
    assert review.review_body == data[0]["review_body"]
    assert review.score == data[0]["score"]


def test_create_review(monkeypatch, test_client, test_database):
    review = Review(product_id=1, user_id=1, review_body='test', score=4)
    test_database.session.add(review)
    test_database.session.commit()

    import requests


    def side_effect_get(url):
        if "users" in url:
            return request_get_user_200(url)
        elif "products" in url:
            return request_get_product_200(url)
        elif "purchase-orders" in url:
            return request_get_purchase_order_200(url)
        else:
            raise ValueError("Unknown URL in get method")
   
    monkeypatch.setattr(
        requests,
        "get",
        side_effect_get
    )

    def side_effect_put(url,json):
        if "score" in url:
            return request_update_product_score_204(url,json)
        else:
            raise ValueError("Unknown URL in put method")

    monkeypatch.setattr(
        requests,
        "put",
        side_effect_put
    )

    resp = test_client.post(
        "/reviews/1",
        data=json.dumps(
            {
                "description": "test",
                "user_id": 1,
                "score": 4,
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 201
    assert data["product_id"] == review.product_id
    assert data["user_id"] == review.user_id
    assert data["review_body"] == review.review_body
    assert data["score"] == review.score
