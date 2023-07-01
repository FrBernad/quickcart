import pytest
import json
from src.api.persistence.user_dao_impl import UserDaoImpl
from src.api.persistence.db import db
from src.api.models.users import User
from unittest.mock import patch, MagicMock
from src.api.services.user_service_impl import UserServiceImpl


def test_get_user_by_email(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_db_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock(return_value=mock_user)
    first_mock.first = lambda: mock_user
    query_mock.filter_by = lambda email: first_mock
    user_db_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.user_dao_impl.User", user_db_mock)

    user_dao, db_mock = test_user_dao

    user = user_dao.get_user_by_email(mock_user.email)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username


def test_get_user_by_id(monkeypatch, test_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    user_db_mock = MagicMock()
    query_mock = MagicMock()
    first_mock = MagicMock(return_value=mock_user)
    first_mock.first = lambda: mock_user
    query_mock.filter_by = lambda id: first_mock
    user_db_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.user_dao_impl.User", user_db_mock)

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
