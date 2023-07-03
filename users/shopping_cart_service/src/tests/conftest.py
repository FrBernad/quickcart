import pytest
from src.api.persistence.db import db
from src import create_app
from unittest.mock import Mock


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app.test_client()


@pytest.fixture(scope="function")
def test_shopping_cart_dao():
    from src.api.persistence.shopping_cart_dao_impl import ShoppingCartDaoImpl

    db_mock = Mock()
    db_session = Mock()
    db_commit = Mock()
    db_add = Mock()
    db_session.commit = db_commit
    db_session.add = db_add
    db_mock.session = db_session
    dao = ShoppingCartDaoImpl(db_mock)
    yield dao, db_mock


@pytest.fixture(scope="module")
def test_shopping_cart_service():
    from src.api.services.shopping_cart_service_impl import ShoppingCartServiceImpl

    shopping_cart_dao_mock = Mock(spec=ShoppingCartServiceImpl)
    service = ShoppingCartServiceImpl(shopping_cart_dao_mock)
    yield service, shopping_cart_dao_mock


@pytest.fixture(scope="function")
def test_database():
    from src.api.models.shopping_cart_product import ShoppingCartProduct

    db.drop_all()
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
