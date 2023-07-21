import pytest
from src.api.models.categories import Category
import json


def test_create_category(test_client, test_database):

    resp = test_client.post(
        "/categories",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria 1",
            }
        ),
    )

    assert resp.status_code == 201
    data = json.loads(resp.data)
    assert 1 == data['id']
    assert "Categoria 1" == data['name']

def test_update_category_by_id_non_existent(test_client, test_database):

    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria X",
            }
        ),
    )

    assert resp.status_code == 404


def test_get_categories(test_client, test_database):
    category1 = Category(id=1,name="Categoria 1")
    test_database.session.add(category1)
    test_database.session.commit()
    category2 = Category(id=2,name="Categoria 2")
    test_database.session.add(category2)
    test_database.session.commit()

    resp = test_client.get(
        "/categories",
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == 2


def test_update_category_by_id(test_client, test_database):
    category = Category(name="Categoria 1")
    test_database.session.add(category)
    test_database.session.commit()
    category.id = 1

    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria X",
            }
        ),
    )

    assert resp.status_code == 204


def test_update_category_by_id_missing_name(test_client, test_database):
    category = Category(name="Categoria 1")
    test_database.session.add(category)
    test_database.session.commit()
    category.id = 1

    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps(
            {}
        ),
    )

    assert resp.status_code == 400


def test_update_category_by_id_non_existent(test_client, test_database):


    resp = test_client.put(
        "/categories/1",
        content_type="application/json",
        data=json.dumps(
            {
                "name": "Categoria X",
            }
        ),
    )

    assert resp.status_code == 404


def test_get_category_by_id(test_client, test_database):
    category = Category(name="Categoria 1")
    test_database.session.add(category)
    test_database.session.commit()
    category.id = 1

    resp = test_client.get(
        "/categories/1"
    )

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert category.id == data['id']
    assert category.name == data['name']


def test_get_category_by_id_non_existent(test_client, test_database):
 
    resp = test_client.get(
        "/categories/1",
        content_type="application/json",
    )

    assert resp.status_code == 404
