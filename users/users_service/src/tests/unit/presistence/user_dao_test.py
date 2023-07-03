import pytest
from src.api.models.users import User
from unittest.mock import MagicMock


def test_get_user_by_email(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock(return_value=mock_user)
    first_mock.first = lambda: mock_user
    query_mock.filter_by = lambda email: first_mock
    user_db_model_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.user_dao_impl.User", user_db_model_mock)

    user_dao, db_mock = test_user_dao

    user = user_dao.get_user_by_email(mock_user.email)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username


def test_get_user_by_id(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_db_model_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock(return_value=mock_user)
    first_mock.first = lambda: mock_user
    query_mock.filter_by = lambda id: first_mock
    user_db_model_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.user_dao_impl.User", user_db_model_mock)

    user_dao, db_mock = test_user_dao

    user = user_dao.get_user_by_id(mock_user.id)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username


def test_create_user(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_dao, db_mock = test_user_dao

    user = user_dao.create_user(mock_user.username, mock_user.email, mock_user.password)

    assert user.email == mock_user.email
    assert user.username == mock_user.username

    db_mock.session.commit.assert_called_once()
    db_mock.session.add.assert_called_once()


def test_update_user(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_dao, db_mock = test_user_dao

    new_username = "new username"
    new_password = "new_password"
    user = user_dao.update_user(mock_user, new_username, new_password)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == new_username

    db_mock.session.commit.assert_called_once()
