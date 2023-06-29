# import pytest
# import json
# from src.api.persistence.user_dao_impl import UserDaoImpl
#
#
# ## --------       CREATE USER     --------
#
# def test_get_user(test_service, monkeypatch):
#     def mock_get_user_by_id(self, id):
#         return {
#             "id": "1",
#             "username": "test",
#             "email": "test@test.com",
#         }
#
#     monkeypatch.setattr(UserDaoImpl, "get_user_by_id", mock_get_user_by_id)
#     user = test_service.get_user_by_id(1)
#
#
#     assert True
#
#     # assert user =
#
#     # user.id  resp.status_code == 201
#     # assert user.id == id
#     # assert user.username == data["username"]
#     # assert "test@test.com" == data["email"]
#     # assert "password" not in data
