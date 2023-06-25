import pytest
from flask_restx import Namespace

from src import create_app,db
from src.api.models.users import User


PACT_DIR = "src/tests/pacts"

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    # app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture(scope="module")
def test_namespace():
    ns = Namespace("testing")
    yield ns

@pytest.fixture(scope="module")
def test_database():
    db.drop_all()
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_user():
    def _add_user(username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
