import pytest
from src.api.persistence.db import db
from src import create_app
from unittest.mock import Mock


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app.test_client()


@pytest.fixture(scope="function")
def test_review_dao():
    from src.api.persistence.review_dao_impl import ReviewDaoImpl

    db_mock = Mock()
    db_session = Mock()
    db_commit = Mock()
    db_add = Mock()
    db_session.commit = db_commit
    db_session.add = db_add
    db_mock.session = db_session
    dao = ReviewDaoImpl(db_mock)
    yield dao, db_mock


@pytest.fixture(scope="module")
def test_review_service():
    from src.api.services.review_service_impl import ReviewServiceImpl
    from src.api.persistence.review_dao_impl import ReviewDaoImpl

    review_dao_mock = Mock(spec=ReviewDaoImpl)
    service = ReviewServiceImpl(review_dao_mock)
    yield service, review_dao_mock


@pytest.fixture(scope="function")
def test_database():
    from src.api.models.reviews import Review

    db.drop_all()
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
