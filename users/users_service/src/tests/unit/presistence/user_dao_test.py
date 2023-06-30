# import pytest
# import json
# from src.api.persistence.user_dao_impl import UserDaoImpl
# from src.api.persistence.db import db
# from src.api.models.users import User
# from unittest.mock import patch, MagicMock
# from src.api.services.user_service_impl import UserServiceImpl


# def test_get_user_by_email(monkeypatch, test_user_dao):
#     mock_user = User(username="test", email="test@test.com", password="12345678")
#     mock_user.id = 1

#     def mock_get_user_by_email(email):
#         return mock_user

#     user_dao, db_mock = test_user_dao

#     monkeypatch.setattr('src.api.models.users.User', MagicMock())

#     user = user_dao.get_user_by_email(mock_user.email)

#     assert user.id == mock_user.id
#     assert user.email == mock_user.email
#     assert user.username == mock_user.username
#     assert user.password == mock_user.password


# # def test_get_user_by_id(monkeypatch, test_user_dao):
# #     mock_user = User(username="test", email="test@test.com", password="12345678")
# #     mock_user.id = 1

# #     def mock_get_user_by_id(id):
# #         return [mock_user]

# #     user_dao, db_mock = test_user_dao

# #     monkeypatch.setattr(User.query, "filter_by", mock_get_user_by_id)

# #     user = user_dao.get_user_by_id(1)

# #     assert user.id == mock_user.id
# #     assert user.email == mock_user.email
# #     assert user.username == mock_user.username
# #     assert user.password == mock_user.password


# # def test_create_user(monkeypatch, test_user_dao):
# #     mock_user = User(username="test", email="test@test.com", password="12345678")
# #     mock_user.id = 1

# #     def mock_create_user(username, email, password):
# #         return mock_user

# #     user_dao, db_mock = test_user_dao

# #     user = user_dao.create_user(mock_user.username, mock_user.email, mock_user.password)

# #     assert user.id == mock_user.id
# #     assert user.email == mock_user.email
# #     assert user.username == mock_user.username
# #     assert user.password == mock_user.password


# # def test_update_user(monkeypatch, test_user_dao):
# #     mock_user = User(username="test", email="test@test.com", password="12345678")
# #     mock_user.id = 1

# #     def mock_update_user(user, username, password):
# #         return mock_user

# #     user_dao, db_mock = test_user_dao

# #     new_username = "new username"
# #     new_password = "new_password"
# #     user = user_dao.update_user(mock_user, new_username, new_password)

# #     assert user.id == mock_user.id
# #     assert user.email == mock_user.email
# #     assert user.username == new_username
# #     assert user.password == new_password
