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

def test_get_purchase_orders(monkeypatch, test_purchase_order_dao):
    
    purchase_order = PurchaseOrders(comments="Comentario",
                                    user_id="1",
                                    total_price=328.32,
                                    payment_method=PaymentMethod.CREDIT_CARD,
                                    card_number="1234567891012345",
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
                           product_price=148.21,
                           product_quantity=1)

    purchase_order.products.append(p1)
    purchase_order.products.append(p2)
    
    purchase_db_model_mock  = MagicMock()
    query_mock = MagicMock()
    all_mock = MagicMock(return_value = purchase_order)
    all_mock.all = lambda: purchase_order
    query_mock.all = lambda: all_mock
    purchase_db_model_mock.query = query_mock
    monkeypatch.setattr("src.api.persistence.purchase_order_dao_impl.PurchaseOrders", purchase_db_model_mock)

    purchase_dao, db_mock = test_purchase_order_dao

    orders = purchase_dao.get_purchase_orders()

    # Assertions
    assert orders.user_id == 1
    # assert orders.id == mock_order.purchase_order_id

def test_get_purchase_order_by_user_id(monkeypatch, test_purchase_order_dao):

    purchase_order = PurchaseOrders(comments="Comentario",
                                    user_id="1",
                                    total_price=328.32,
                                    payment_method=PaymentMethod.CREDIT_CARD,
                                    card_number="1234567891012345",
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
                           product_price=148.21,
                           product_quantity=1)

    mock_user_id = 1
    purchase_order.products.append(p1)
    purchase_order.products.append(p2)
    
    purchase_db_model_mock = MagicMock()
    query_mock = MagicMock()
    filter_mock = MagicMock(return_value = purchase_order)
    query_mock.filter = lambda user_id: purchase_order
    query_mock.filter = lambda: filter_mock
    purchase_db_model_mock.query = query_mock

    monkeypatch.setattr("src.api.persistence.purchase_order_dao_impl.PurchaseOrders", purchase_db_model_mock)

    purchase_dao, db_mock = test_purchase_order_dao

    orders = purchase_dao.get_purchase_order_by_user_id(mock_user_id)

    assert 1 == 1

def test_create_purchase_order_with_products(monkeypatch, test_purchase_order_dao):
     
    purchase_order = PurchaseOrders(comments="Comentario",
                                    user_id="1",
                                    total_price=328.32,
                                    payment_method=PaymentMethod.CREDIT_CARD,
                                    card_number="1234 5678 9012 3456",
                                    expiration_year=2025,
                                    expiration_month=7,
                                    cvv=123,
                                    card_type=CardType.VISA,
                                    purchase_order_id=1)

    p1 = ProductsPurchased(purchase_order=purchase_order,
                           product_id="1",
                           product_price=127.21,
                           product_quantity=2)

    p2 = ProductsPurchased(purchase_order=purchase_order,
                           product_id="2",
                           product_price=148.21,
                           product_quantity=1)

    purchase_order.products.append(p1)
    purchase_order.products.append(p2)

    payment_details = PaymentDetails(
        payment_method="credit_card",
        card_number="1234 5678 9012 3456",
        expiration_year="2025",
        expiration_month="07",
        cvv="123",
        card_type=CardType.VISA
        )

    purchase_dao, db_mock = test_purchase_order_dao

    purchase = purchase_dao.create_purchase_order_with_products(purchase_order.user_id, 
                                                                purchase_order.total_price, 
                                                                purchase.products,
                                                                payment_details)
    assert purchase.comments == purchase_order.comments
    assert purchase.total_price == purchase_order.total_price
    assert purchase.payment_method == purchase_order.payment_method

    db_mock.session.commit.assert_called_once()
    db_mock.session.add.assert_called_once()