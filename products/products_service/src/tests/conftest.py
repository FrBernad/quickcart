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
def test_product_dao():
    from src.api.persistence.product_dao_impl import ProductDaoImpl

    db_mock = Mock()
    db_session = Mock()
    db_commit = Mock()
    db_add = Mock()
    db_session.commit = db_commit
    db_session.add = db_add
    db_mock.session = db_session
    dao = ProductDaoImpl(db_mock)
    yield dao, db_mock


@pytest.fixture(scope="module")
def test_product_service():
    from src.api.services.product_service_impl import ProductServiceImpl
    from src.api.persistence.product_dao_impl import ProductDaoImpl

    product_dao_mock = Mock(spec=ProductDaoImpl)
    service = ProductServiceImpl(product_dao_mock)
    yield service, product_dao_mock


@pytest.fixture(scope="function")
def test_database():
    from src.api.models.product import Product
    from src.api.models.tag import Tag

    db.drop_all()
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
