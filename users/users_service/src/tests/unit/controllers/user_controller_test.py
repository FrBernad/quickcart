import pytest
import json
from src.api.services.user_service_impl import UserServiceImpl

# def test_create_user(test_client, monkeypatch):
#     pass

def test_get_existing_user_by_id(test_client, monkeypatch):
    def mock_get_user_by_id(self, user_id):
        return {
            "id": "1",
            "username": "test",
            "email": "test@test.com",
        }
    
    monkeypatch.setattr(UserServiceImpl, "get_user_by_id", mock_get_user_by_id)
    resp = test_client.get("/users/1")

    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 1 == data["id"]
    assert "test" == data["username"]
    assert "test@test.com" == data["email"]
    assert "password" not in data


# def test_update_user(test_client, monkeypatch):
#     pass
