import pytest
import json
from src.api.services.user_service_impl import UserService



def test_testing():
    pass

# def test_create_user(test_client, monkeypatch):
#     pass


# def test_get_existing_user(test_client, monkeypatch):
    # def mock_get_user_by_id(user_id):
    #     return {
    #         "id": 1,
    #         "name": "test",
    #         "email": "test@test.com",
    #     }

    # monkeypatch.setattr(UserService, "get_user_by_id", mock_get_user_by_id)
    # resp = test_client.get("/users/1")

    # data = json.loads(resp.data.decode())
    # assert resp.status_code == 200
    # assert "1" in data["id"]
    # assert "test" in data["username"]
    # assert "test@test.com" in data["email"]
    # assert "password" not in data


# def test_update_user(test_client, monkeypatch):
#     pass
