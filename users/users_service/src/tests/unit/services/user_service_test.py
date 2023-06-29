import pytest
import json
from src.api.interfaces.persistence.user_dao import UserDao
from src.api.models.users import User
from src.api.services.user_service_impl import UserServiceImpl


# ## --------       CREATE USER     --------


def test_get_user_by_email(mock_user_dao):
    mock_user = User(username="test", email="test@test.com", password="12345678")
    mock_user.id = 1
    # Configure the mock behavior as needed
    mock_user_dao.get_user_by_email.return_value = mock_user

    # Create a UserService instance with the mock UserDAO
    user_service = UserServiceImpl(user_dao=mock_user_dao)

    # Test the UserService behavior
    user = user_service.get_user_by_email("test@test.com")

    # Assert the expected result based on the mock configuration
    assert user.id == mock_user.id
