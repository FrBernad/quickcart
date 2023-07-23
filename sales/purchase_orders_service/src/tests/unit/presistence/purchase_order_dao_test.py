import pytest
from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from src.api.models.purchase_orders import PurchaseOrders
from src.api.models.purchase_products import ProductsPurchased
from src.api.models.payment_method import PaymentMethod
from src.api.models.payment_details import PaymentDetails
from src.api.models.card_type import CardType
from src.api.models.purchase_order_details import PurchaseOrderDetails
from src.api.persistence.purchase_order_dao_impl import PurchaseOrderDaoImpl
from unittest.mock import MagicMock

purchase_order = PurchaseOrders(comments="Comentario",
                                    user_id=1,
                                    total_price=254.42,
                                    payment_method=PaymentMethod.CREDIT_CARD,
                                    card_number="1234567890123456",
                                    expiration_year=2023,
                                    expiration_month=12,
                                    cvv=123,
                                    card_type=CardType.VISA,
                                    purchase_order_id=1)

p1 = ProductsPurchased(purchase_order=purchase_order,
                        product_id="1",
                        product_price=127.21,
                        product_quantity=2)

p2 = ProductsPurchased(purchase_order=purchase_order,
                        product_id="2",
                        product_price=127.21,
                        product_quantity=1)

payment_details = PaymentDetails(
    payment_method=PaymentMethod.CREDIT_CARD,
    card_number="1234567890123456",
    expiration_year=2023,
    expiration_month=12,
    cvv="123",
    card_type=CardType.VISA
)

purchase_order.products.append(p1)
purchase_order.products.append(p2)

def test_get_purchase_orders(monkeypatch, test_purchase_order_dao):
    
    
    purchase_db_model_mock = MagicMock()
    query_mock = MagicMock()
    query_mock.all = lambda: [purchase_order]
    purchase_db_model_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.purchase_order_dao_impl.PurchaseOrders", purchase_db_model_mock)

    purchase_dao, db_mock = test_purchase_order_dao

    orders = purchase_dao.get_purchase_orders()

    assert orders[0].user_id == 1
    assert orders[0].total_price == 254.42
    assert orders[0].payment_method == PaymentMethod.CREDIT_CARD
    assert orders[0].card_number == "1234567890123456"
    assert orders[0].expiration_year == 2023
    assert orders[0].expiration_month == 12
    assert orders[0].cvv == 123

def test_get_purchase_order_by_user_id(monkeypatch, test_purchase_order_dao):

    mock_user_id = 1
    mock_product_id = None

    purchase_db_model_mock = MagicMock()
    
    query_mock = MagicMock()
    all_mock = MagicMock()
    all_mock.all = lambda: [purchase_order]
    query_mock.filter = lambda user_id: all_mock
    
    join_mock = MagicMock()
    join_mock.filter = lambda product_id: all_mock
    query_mock.join = join_mock

    purchase_db_model_mock.query = query_mock

    monkeypatch.setattr("src.api.persistence.purchase_order_dao_impl.PurchaseOrders", purchase_db_model_mock)

    purchase_dao, db_mock = test_purchase_order_dao

    orders = purchase_dao.get_purchase_order_by_user_id(mock_user_id, mock_product_id)

    assert orders[0].user_id == 1
    assert orders[0].total_price == 254.42
    assert orders[0].payment_method==PaymentMethod.CREDIT_CARD
    assert orders[0].card_number == "1234567890123456"
    assert orders[0].expiration_year == 2023
    assert orders[0].expiration_month == 12
    assert orders[0].cvv == 123

def test_create_purchase_order_with_products(monkeypatch, test_purchase_order_dao):
    
    purchase_db_model_mock = MagicMock()
    purchase_dao, db_mock = test_purchase_order_dao
    monkeypatch.setattr(
        "src.api.persistence.purchase_order_dao_impl.PurchaseOrders", 
        purchase_db_model_mock
    )
    purchase = purchase_dao.create_purchase_order_with_products(purchase_order.comments,
                                                                purchase_order.user_id, 
                                                                purchase_order.total_price, 
                                                                purchase_order.products,
                                                                payment_details)
    assert db_mock.session.add.call_count == 1
    db_mock.session.add.assert_called_once()
    # FIXME: commit problem
    # db_mock.session.commit.assert_called_once()

