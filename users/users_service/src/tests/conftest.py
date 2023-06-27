import pytest
from src.api.persistence.db import db
from src import create_app

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    with app.app_context():
        yield app.test_client()

@pytest.fixture(scope="module")
def test_database(test_client):
    from src.api.models.users import User
    db.drop_all()
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()