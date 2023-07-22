import pytest
from src.api.models.reviews import Review
from unittest.mock import MagicMock


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def test_get_reviews_by_product(test_review_service):
    mock_reviews = [Review(product_id=1, user_id=1, review_body="test", score=4)]

    def mock_get_reviews_by_product(product_id):
        return mock_reviews

    review_service, review_dao_mock = test_review_service

    review_dao_mock.get_reviews_by_product = mock_get_reviews_by_product

    reviews = review_service.get_reviews_by_product(1)

    assert len(reviews) == len(mock_reviews)
    assert reviews[0].product_id == mock_reviews[0].product_id
    assert reviews[0].user_id == mock_reviews[0].user_id
    assert reviews[0].review_body == mock_reviews[0].review_body
    assert reviews[0].score == mock_reviews[0].score

def test_get_review_by_id(test_review_service):
    mock_review = Review(product_id=1, user_id=1, review_body="test", score=4)

    def mock_get_review_by_id(review_id):
        return mock_review

    review_service, review_dao_mock = test_review_service

    review_dao_mock.get_review_by_id = mock_get_review_by_id

    review = review_service.get_review_by_id(1)

    assert review.product_id == mock_review.product_id
    assert review.user_id == mock_review.user_id
    assert review.review_body == mock_review.review_body
    assert review.score == mock_review.score


def test_create_review(monkeypatch, test_review_service):
    mock_review = Review(product_id=1, user_id=1, review_body="test", score=4)

    import requests

    def request_get_purchase_order(url):
        return MockResponse([], 200)

    monkeypatch.setattr(
        requests,
        "get",
        request_get_purchase_order
    )

    def mock_create_review(product_id, user_id, review_body, score):
        return mock_review

    review_service, review_dao_mock = test_review_service

    review_dao_mock.add_product = MagicMock(spec=mock_create_review)

    review_service.create_review(1, 1, "test", 4)

    review_dao_mock.create_review.assert_called()
