import pytest
import json
from src.api.models.users import User


## --------       CREATE USER     --------


def test_create_user(test_client, test_database):
    user = User(username="test", email="test@test.com", password="12345678")
    user.id = 1

    resp = test_client.post(
        "/users",
        data=json.dumps(
            {
                "username": "test",
                "email": "test@test.com",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 201
    assert user.id == data["id"]
    assert user.username == data["username"]
    assert user.email == data["email"]
    assert "password" not in data


def test_create_user_with_email_already_register(test_client, test_database):
    user = User(username="test", email="test@test.com", password="12345678")
    test_database.session.add(user)
    test_database.session.commit()

    resp = test_client.post(
        "/users",
        data=json.dumps(
            {
                "username": "test",
                "email": "test@test.com",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert f"The email test@test.com is already in use." == data["message"]


def test_create_user_missing_username(test_client, test_database):
    resp = test_client.post(
        "/users",
        data=json.dumps(
            {
                "email": "test@test.com",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_create_user_missing_password(test_client, test_database):
    resp = test_client.post(
        "/users",
        data=json.dumps(
            {
                "username": "test",
                "email": "test@test.com",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_create_user_missing_email(test_client, test_database):
    resp = test_client.post(
        "/users",
        data=json.dumps(
            {
                "username": "test",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    print(data)
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


## --------       GET USER     --------


def test_get_existing_user_by_id(test_client, test_database):
    user = User(username="test", email="test@test.com", password="12345678")
    test_database.session.add(user)
    test_database.session.commit()

    resp = test_client.get("/users/1")

    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 1 == data["id"]
    assert "test" == data["username"]
    assert "test@test.com" == data["email"]
    assert "password" not in data


def test_get_non_existing_user_by_id(test_client, test_database):
    resp = test_client.get("/users/1")

    data = json.loads(resp.data.decode())
    assert resp.status_code == 404


## --------       UPDATE USER     --------


def test_update_user(test_client, test_database):
    user = User(username="test", email="test@test.com", password="12345678")
    test_database.session.add(user)
    test_database.session.commit()
    
    user_updated = User(username="test2", email="test@test.com", password="123456789")

    resp = test_client.put(
        "/users/1",
        data=json.dumps(
            {
                "username": "test",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 204
    assert not resp.data


def test_update_not_existing_user(test_client, test_database):
    resp = test_client.put(
        "/users/1",
        data=json.dumps(
            {
                "username": "test",
                "email": "test@test.com",
                "password": "12345678",
            }
        ),
        content_type="application/json",
    )

    assert resp.status_code == 404
