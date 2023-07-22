import pytest
from src.api.models.reviews import Review
from unittest.mock import MagicMock


def test_get_reviews_by_product(monkeypatch, test_review_dao):
    mock_reviews = [Review(product_id=1, user_id=1, review_body="test", score=1)]

    review_db_model_mock = MagicMock()
    query_mock = MagicMock()
    all_mock = MagicMock()
    all_mock.all = lambda: mock_reviews
    query_mock.filter_by = lambda product_id: all_mock
    review_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.review_dao_impl.Review",
        review_db_model_mock,
    )

    review_dao, db_mock = test_review_dao

    product_id = 1

    reviews = review_dao.get_reviews_by_product(product_id)

    assert len(mock_reviews) == len(reviews)
    assert mock_reviews[0].product_id == reviews[0].product_id
    assert mock_reviews[0].user_id == reviews[0].user_id
    assert mock_reviews[0].review_body == reviews[0].review_body
    assert mock_reviews[0].score == reviews[0].score

def test_get_review_by_id(monkeypatch, test_review_dao):
    mock_review = Review(product_id=1, user_id=1, review_body="test", score=1)

    review_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock()
    first_mock.first = lambda: mock_review
    query_mock.filter_by = lambda id: first_mock
    review_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.review_dao_impl.Review",
        review_db_model_mock,
    )

    review_dao, db_mock = test_review_dao

    review_id = 1

    review = review_dao.get_review_by_id(review_id)

    assert mock_review.user_id == review.user_id
    assert mock_review.review_body == review.review_body
    assert mock_review.score == review.score


def test_create_review(monkeypatch, test_review_dao):
    review_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock()
    first_mock.first = lambda: []
    query_mock.filter_by = lambda review_id: first_mock
    review_db_model_mock.query = query_mock
    monkeypatch.setattr(
        "src.api.persistence.review_dao_impl.Review",
        review_db_model_mock,
    )

    review_dao, db_mock = test_review_dao

    product_id = 1
    user_id = 1
    review_body = 1
    score = 3

    review_dao.create_review(product_id, user_id, review_body, score)

    db_mock.session.add.assert_called_once()
    db_mock.session.commit.assert_called_once()
