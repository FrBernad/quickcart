import pytest
from src.api.models.reviews import Review
from unittest.mock import MagicMock
from src.tests.mocks import (
    request_get_user_200,
    request_get_product_200,
    request_get_purchase_order_200,
    request_update_product_score_204,
)

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
    reviews_qty = 0

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

    def mock_create_review(product_id, user_id, review_body, score):
        return mock_review
    
    def request_get_reviews_quantity_by_product(product_id):
        return reviews_qty

    review_service, review_dao_mock = test_review_service

    review_dao_mock.create_review = MagicMock(spec=mock_create_review)
    review_dao_mock.get_reviews_quantity_by_product = MagicMock(spec=request_get_reviews_quantity_by_product,return_value=reviews_qty)

    review = review_service.create_review(1, 1, "test", 4)
    review_dao_mock.create_review.assert_called()




