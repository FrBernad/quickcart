import pytest
from src.api.services.review_service_impl import ReviewServiceImpl
from src.api.models.reviews import Review
import json


def test_get_reviews_by_product(test_client, monkeypatch):
    mock_reviews = [Review(product_id=1, user_id=1, review_body='test', score=4)]

    def mock_get_reviews_by_product(self, product_id):
        return mock_reviews

    monkeypatch.setattr(ReviewServiceImpl, "get_reviews_by_product", mock_get_reviews_by_product)

    resp = test_client.get(
        "/reviews?product_id=1",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(mock_reviews) == len(data)
    assert mock_reviews[0].product_id == data[0]["product_id"]
    assert mock_reviews[0].user_id == data[0]["user_id"]
    assert mock_reviews[0].review_body == data[0]["review_body"]
    assert mock_reviews[0].score == data[0]["score"]

def test_create_review(test_client, monkeypatch):
    mock_review = Review(product_id=1, user_id=1, review_body='test', score=4)

    def mock_create_review(self, product_id, user_id, review_body, score):
        return mock_review

    monkeypatch.setattr(ReviewServiceImpl, "create_review", mock_create_review)

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
    assert data["product_id"] == mock_review.product_id
    assert data["user_id"] == mock_review.user_id
    assert data["review_body"] == mock_review.review_body
    assert data["score"] == mock_review.score
