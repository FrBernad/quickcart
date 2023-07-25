import pytest
from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from src.api.services.purchase_order_service_impl import PurchaseOrderServiceImpl
from src.api.models.purchase_orders import PurchaseOrders
from src.api.models.purchase_products import ProductsPurchased
from src.api.models.card_type import CardType
from src.api.models.payment_method import PaymentMethod
from src.api.models.payment_details import PaymentDetails

from src.tests.mocks import (
    request_get_product_200,
)

def test_get_purchase_orders(monkeypatch,test_purchase_order_service):

    
    import requests

    def side_effect_get(url):
        if "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(requests, "get", side_effect_get)

    
    purchase_order1 = PurchaseOrders(comments="Comentario",
                                     user_id="1",
                                     total_price=328.32,
                                     payment_method=PaymentMethod.CREDIT_CARD,
                                     card_number="1234567891012345",
                                     expiration_year=2023,
                                     expiration_month=12,
                                     cvv=123,
                                     card_type=CardType.VISA,
                                     purchase_order_id=1)
    purchase_order2 = PurchaseOrders(comments="Comentario2",
                                     user_id="2",
                                     total_price=313,
                                     payment_method=PaymentMethod.CREDIT_CARD,
                                     card_number="1234512345678910",
                                     expiration_year=2024,
                                     expiration_month=1,
                                     cvv=124,
                                     card_type=CardType.MASTERCARD,
                                     purchase_order_id=2)

    p1 = ProductsPurchased(purchase_order=purchase_order1,
                           product_id="1",
                           product_price=127.21,
                           product_quantity=2)

    p2 = ProductsPurchased(purchase_order=purchase_order1,
                           product_id="2",
                           product_price=148.21,
                           product_quantity=1)
    p3 = ProductsPurchased(purchase_order=purchase_order2,
                           product_id="1",
                           product_price=127.21,
                           product_quantity=2)

    p4 = ProductsPurchased(purchase_order=purchase_order2,
                           product_id="2",
                           product_price=148.21,
                           product_quantity=1)

    purchase_order1.products.append(p1)
    purchase_order1.products.append(p2)
    purchase_order2.products.append(p3)
    purchase_order2.products.append(p4)

    def mock_get_purchase_orders():
        return [purchase_order1, purchase_order2]
    
    purchase_service, purchase_dao_mock = test_purchase_order_service

    purchase_dao_mock.get_purchase_orders = mock_get_purchase_orders

    purchase_orders = purchase_service.get_purchase_orders()

    assert len(purchase_orders) == 2


def test_get_purchase_order_by_user_id(monkeypatch,test_purchase_order_service):

    import requests

    def side_effect_get(url):
        if "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(requests, "get", side_effect_get)

    mock_user_id = "1"
    purchase_order1 = PurchaseOrders(comments="Comentario",
                                     user_id=mock_user_id,
                                     total_price=328.32,
                                     payment_method=PaymentMethod.CREDIT_CARD,
                                     card_number="1234567891012345",
                                     expiration_year=2023,
                                     expiration_month=12,
                                     cvv=123,
                                     card_type=CardType.VISA,
                                     purchase_order_id=1)

    p1 = ProductsPurchased(purchase_order=purchase_order1,
                           product_id="1",
                           product_price=127.21,
                           product_quantity=2)

    purchase_order1.products.append(p1)

    def mock_get_purchase_order_by_user_id(user_id, product_id):
        return [purchase_order1]
    
    purchase_service, purchase_dao_mock = test_purchase_order_service

    purchase_dao_mock.get_purchase_order_by_user_id = mock_get_purchase_order_by_user_id

    purchase_orders = purchase_service.get_purchase_order_by_user_id(mock_user_id)

    assert purchase_orders[0].user_id == mock_user_id
    assert purchase_orders[0].comments == "Comentario"
    assert purchase_orders[0].total_price == 328.32
    assert purchase_orders[0].card_number == "1234567891012345"
    assert purchase_orders[0].expiration_year == 2023
    assert purchase_orders[0].expiration_month == 12
    assert purchase_orders[0].cvv == 123
    assert purchase_orders[0].purchase_order_id == 1



def test_create_purchase_order(monkeypatch,test_purchase_order_service):

    import requests

    def side_effect_get(url):
        if "products" in url:
            return request_get_product_200(url)
        else:
            raise ValueError("Unknown URL in get method")

    monkeypatch.setattr(requests, "get", side_effect_get)

    purchase_order1 = PurchaseOrders(comments="Comentario",
                                     user_id=1,
                                     total_price=328.32,
                                     payment_method=PaymentMethod.CREDIT_CARD,
                                     card_number="1234567891012345",
                                     expiration_year=2023,
                                     expiration_month=12,
                                     cvv=123,
                                     card_type=CardType.VISA,
                                     purchase_order_id=1)

    p1 = ProductsPurchased(purchase_order=purchase_order1,
                           product_id=1,
                           product_price=127.21,
                           product_quantity=2)

    payment_details = PaymentDetails(
        payment_method="Credit Card",
        card_number="1234 5678 9012 3456",
        expiration_year=2025,
        expiration_month=12,
        cvv="123",
        card_type="Visa"
    )

    purchase_order1.products.append(p1)

    def mock_create_purchase_order(comments, user_id, total_price, products, payment_details):
        return purchase_order1

    purchase_service, purchase_dao_mock = test_purchase_order_service

    purchase_dao_mock.create_purchase_order_with_products = mock_create_purchase_order

    order_created = purchase_service.create_purchase_order( purchase_order1.comments, 
                                                            purchase_order1.user_id, 
                                                            purchase_order1.total_price,
                                                            purchase_order1.products,
                                                            payment_details)
    assert order_created.user_id == 1
    assert order_created.comments == "Comentario"
    assert order_created.total_price == 328.32
    assert order_created.card_number == "1234567891012345"
    assert order_created.expiration_year == 2023
    assert order_created.expiration_month == 12
    assert order_created.cvv == 123
    assert order_created.purchase_order_id == 1
