import pytest
from src.api.persistence.db import db
from src import create_app
from unittest.mock import Mock
from src.api.persistence.user_dao_impl import UserDaoImpl


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    with app.app_context():
        yield app.test_client()


@pytest.fixture
def mock_user_dao(monkeypatch):
    # Create a mock UserDAO object
    user_dao_mock = Mock(spec=UserDaoImpl)

    # Patch the UserDAO class with the mock object
    monkeypatch.setattr(UserDaoImpl, '__new__', lambda cls: user_dao_mock)

    # Return the mock UserDAO object
    return user_dao_mock


# @pytest.fixture(scope="module")
# def test_dao(test_database):
#     from src.api.persistence.user_dao_impl import UserDaoImpl
#     service = UserDaoImpl(test_database)
#     yield service


@pytest.fixture(scope="module")
def test_database(test_client):
    from src.api.models.users import User
    db.drop_all()
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
