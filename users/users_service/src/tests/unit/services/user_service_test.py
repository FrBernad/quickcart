import pytest
from src.api.models.users import User
from src.api.interfaces.exceptions.email_already_registered_exception import EmailAlreadyRegisteredException
from src.api.interfaces.exceptions.user_not_found_exception import UserNotFoundException
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

def test_get_user_by_email_non_existent(test_user_service):
    mock_user_email = "test@test.com"

    def mock_get_user_by_email(email):
        return None

    user_service, user_dao_mock = test_user_service

    user_dao_mock.get_user_by_email = mock_get_user_by_email

    user = user_service.get_user_by_email(mock_user_email)

    assert user is None


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


def test_get_user_by_id_non_existent(test_user_service):

    def mock_get_user_by_id(user_id):
        return None

    user_service, user_dao_mock = test_user_service

    user_dao_mock.get_user_by_id = mock_get_user_by_id

    with pytest.raises(UserNotFoundException):
        user = user_service.get_user_by_id(1)


def test_create_user(test_user_service):
    mock_user_email = "test@test.com"

    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_email(email):
        return None

    def mock_create_user(username, email, password):
        return mock_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.create_user = mock_create_user
    user_dao_mock.get_user_by_email = mock_get_user_by_email

    user = user_service.create_user(
        mock_user.username, mock_user.email, mock_user.password
    )

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == mock_user.username
    assert user.password == mock_user.password


def test_create_user_already_registered(test_user_service):

    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_email(email):
        return mock_user

    def mock_create_user(username, email, password):
        return mock_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.create_user = mock_create_user
    user_dao_mock.get_user_by_email = mock_get_user_by_email


    with pytest.raises(EmailAlreadyRegisteredException):
        user =  user_service.create_user(
        mock_user.username, mock_user.email, mock_user.password
        )

def test_update_user(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_id(user_id):
        return mock_user

    def mock_update_user(user, username, password):
        updated_user = copy.copy(mock_user)
        updated_user.username = username
        updated_user.password = password
        return updated_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.update_user = mock_update_user
    user_dao_mock.get_user_by_id = mock_get_user_by_id

    new_username = "new username"
    new_password = "new_password"

    user = user_service.update_user(mock_user, new_username, new_password)

    assert user.id == mock_user.id
    assert user.email == mock_user.email
    assert user.username == new_username
    assert user.password == new_password


def test_update_user_invalid_id(test_user_service):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1

    def mock_get_user_by_id(user_id):
        return None

    def mock_update_user(user, username, password):
        updated_user = copy.copy(mock_user)
        updated_user.username = username
        updated_user.password = password
        return updated_user

    user_service, user_dao_mock = test_user_service

    user_dao_mock.update_user = mock_update_user
    user_dao_mock.get_user_by_id = mock_get_user_by_id

    new_username = "new username"
    new_password = "new_password"

    with pytest.raises(UserNotFoundException):
        user = user_service.update_user(mock_user, new_username, new_password)