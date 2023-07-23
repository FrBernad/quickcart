import pytest
from src.api.services.category_service_impl import CategoryServiceImpl
from src.api.models.categories import Category
from src.api.interfaces.exceptions.category_not_found_exception import (
    CategoryNotFoundException,
)

import json


def test_get_categories(test_client, monkeypatch):
    assert True == False
    mock_categories = [
        Category(id=1, name="Categoria 1"),
        Category(id=2, name="Categoria 2"),
    ]

    def mock_get_categories(self):
        return mock_categories

    monkeypatch.setattr(CategoryServiceImpl, "get_categories", mock_get_categories)

    resp = test_client.get("/categories", content_type="application/json")

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(mock_categories) == len(data)
    assert mock_categories[0].id == data[0]["id"]
    assert mock_categories[0].name == data[0]["name"]
    assert mock_categories[1].id == data[1]["id"]
    assert mock_categories[1].name == data[1]["name"]


def test_get_category_by_id(test_client, monkeypatch):
    mock_category = Category(id=1, name="Categoria 1")

    def mock_get_category_by_id(self, category_id):
        return mock_category

    monkeypatch.setattr(
        CategoryServiceImpl, "get_category_by_id", mock_get_category_by_id
    )

    resp = test_client.get("/categories/1")

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert mock_category.id == data["id"]
    assert mock_category.name == data["name"]


def test_get_category_by_id_non_existent(test_client, monkeypatch):
    def mock_get_category_by_id(self, category_id):
        raise CategoryNotFoundException(category_id)

    monkeypatch.setattr(
        CategoryServiceImpl, "get_category_by_id", mock_get_category_by_id
    )

    resp = test_client.get("/categories/1")

    assert resp.status_code == 404


def test_create_category(test_client, monkeypatch):
    mock_category = Category(id=1, name="Categoria 1")

    def mock_create_category(self, name):
        return mock_category

    monkeypatch.setattr(CategoryServiceImpl, "create_category", mock_create_category)

    resp = test_client.post(
        "/categories",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria 1",
            }
        ),
    )

    data = json.loads(resp.data)
    assert resp.status_code == 201
    assert data["name"] == mock_category.name
    assert data["id"] == mock_category.id


def test_create_category_missing_name(test_client, monkeypatch):
    def mock_create_category(self, name):
        return None

    monkeypatch.setattr(CategoryServiceImpl, "create_category", mock_create_category)

    resp = test_client.post(
        "/categories",
        data=json.dumps({}),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]


def test_update_category(test_client, monkeypatch):
    mock_category = Category(id=1, name="Categoria 1")

    def mock_update_category(self, category_id, name):
        return mock_category

    monkeypatch.setattr(CategoryServiceImpl, "update_category", mock_update_category)

    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria 1",
            }
        ),
    )

    assert resp.status_code == 204


def test_update_category_missing_name(test_client, monkeypatch):
    def mock_update_category(self, category_id, name):
        return None

    monkeypatch.setattr(CategoryServiceImpl, "update_category", mock_update_category)

    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps({}),
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid input" == data["error"]
