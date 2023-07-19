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
    from src.api.persistence.purchase_order_dao_impl import PurchaseOrderDaoImpl

    db_mock = Mock()
    db_session = Mock()
    db_commit = Mock()
    db_add = Mock()
    db_session.commit = db_commit
    db_session.add = db_add
    db_mock.session = db_session
    dao = PurchaseOrderDaoImpl(db_mock)
    yield dao, db_mock


@pytest.fixture(scope="module")
def test_shopping_cart_service():
    from src.api.services.purchase_order_service_impl import PurchaseOrderServiceImpl

    purchase_order_dao_mock = Mock(spec=PurchaseOrderServiceImpl)
    service = PurchaseOrderServiceImpl(purchase_order_dao_mock)
    yield service, purchase_order_dao_mock


@pytest.fixture(scope="function")
def test_database():
    from src.api.models.purchase_orders import PurchaseOrders
    from src.api.models.purchase_products import ProductsPurchased
    db.drop_all()
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
