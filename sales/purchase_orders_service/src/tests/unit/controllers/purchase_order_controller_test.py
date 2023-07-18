import pytest
import json
from src.api.models.purchase_orders import PurchaseOrders
from src.api.models.purchase_products import ProductsPurchased
from src.api.models.card_type import CardType
from src.api.models.payment_method import PaymentMethod

from src.api.services.purchase_order_service_impl import PurchaseOrderServiceImpl


## --------       CREATE PURCHASE ORDER     --------


def test_create_purchase_order(test_client, monkeypatch):
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

    def mock_create_purchase_order(self, comments,
                                   user_id,
                                   total_price,
                                   products,
                                   payment_details):
        return purchase_order

    monkeypatch.setattr(PurchaseOrderServiceImpl, "create_purchase_order", mock_create_purchase_order)

    resp = test_client.post(
        "/purchase-orders",
        data=json.dumps(
            {
                "comments": "asd",
                "user_id": "1",
                "products": [
                    {
                        "product_id": "1",
                        "product_price": 2.24,
                        "product_quantity": 1
                    },
                    {
                        "product_id": "2",
                        "product_price": 0.93,
                        "product_quantity": 1
                    }

                ],
                "total_price": 12,
                "payment_details": {
                    "payment_method": "CREDIT_CARD",
                    "card_number": "123456789012345",
                    "expiration_year": 2022,
                    "expiration_month": 3,
                    "cvv": "123",
                    "card_type": "VISA"
                }
            }
        ),
        content_type="application/json",
    )

    data = json.loads(resp.data)
    assert resp.status_code == 201
    assert purchase_order.purchase_order_id == data["purchase_order_id"]
    assert purchase_order.cvv == data["cvv"]
    assert purchase_order.comments == data["comments"]
    assert purchase_order.expiration_month == data["expiration_month"]
    assert purchase_order.expiration_year == data["expiration_year"]
    assert purchase_order.card_number == data["card_number"]
    assert purchase_order.card_type == data["card_type"]
    assert purchase_order.payment_method == data["payment_method"]
    assert purchase_order.total_price == data["total_price"]
    assert purchase_order.user_id == data["user_id"]
    assert "products" in data
    # FIXME: faltan comparar los productos


def test_get_purchase_orders(test_client, monkeypatch):
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

    def mock_get_purchase_orders(self):
        return [purchase_order1, purchase_order2]

    monkeypatch.setattr(PurchaseOrderServiceImpl, "get_purchase_orders", mock_get_purchase_orders)

    resp = test_client.get("/purchase-orders")

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert len(data) == 2

    # FIXME: faltan comparar las ordenes de los productos
    # FIXME: faltan comparar los productos


def test_get_purchase_order_by_id(test_client, monkeypatch):
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

    def mock_get_get_purchase_order_by_id(self, purchase_order_id):
        return purchase_order

    monkeypatch.setattr(PurchaseOrderServiceImpl, "get_purchase_order_by_id", mock_get_get_purchase_order_by_id)

    resp = test_client.get("/purchase-orders/1")

    data = json.loads(resp.data)
    assert resp.status_code == 200
    assert purchase_order.purchase_order_id == data["purchase_order_id"]
    assert purchase_order.cvv == data["cvv"]
    assert purchase_order.comments == data["comments"]
    assert purchase_order.expiration_month == data["expiration_month"]
    assert purchase_order.expiration_year == data["expiration_year"]
    assert purchase_order.card_number == data["card_number"]
    assert purchase_order.card_type == data["card_type"]
    assert purchase_order.payment_method == data["payment_method"]
    assert purchase_order.total_price == data["total_price"]
    assert purchase_order.user_id == data["user_id"]
    assert "products" in data
    # FIXME: faltan comparar los productos
