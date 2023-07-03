import pytest
import json
from src.api.persistence.user_dao_impl import UserDaoImpl
from src.api.models.users import User
from src.api.services.user_service_impl import UserServiceImpl
import copy


def test_get_user_by_email(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_email(email):
        return mock_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.get_user_by_email = mock_get_user_by_email

    user = user_service.get_user_by_email(mock_user.email)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username
    assert user.password == mock_user.password


def test_get_user_by_id(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_id(user_id):
        return mock_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.get_user_by_id = mock_get_user_by_id

    user = user_service.get_user_by_id(1)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username
    assert user.password == mock_user.password


def test_create_user(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_create_user(username, email, password):
        return mock_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.create_user = mock_create_user

    user = user_service.create_user(
        mock_user.username, mock_user.email, mock_user.password
    )

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username
    assert user.password == mock_user.password


def test_update_user(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_update_user(user, username, password):
        updated_user = copy.copy(mock_user)
        updated_user.username = username
        updated_user.password = password

        return updated_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.update_user = mock_update_user

    new_username = "new username"
    new_password = "new_password"

    user = user_service.update_user(mock_user, new_username, new_password)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == new_username
    assert user.password == new_password
