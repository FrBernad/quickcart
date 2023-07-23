import pytest
from src.api.models.purchase_orders import PurchaseOrders
from src.api.models.purchase_products import ProductsPurchased
from src.api.models.payment_method import PaymentMethod
from src.api.models.payment_details import PaymentDetails
from src.api.models.card_type import CardType
from src.api.models.purchase_order_details import PurchaseOrderDetails

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

# def test_create_purchase_order(test_client, test_database):

#     resp = test_client.post(
#         "/purchase-orders",
#         data=json.dumps(
#             {
#                 "comments": "Comentario",
#                 "user_id": "1",
#                 "products": [
#                     {
#                         "product_id": "1",
#                         "product_price": 127.21,
#                         "product_quantity": 1
#                     },
#                     {
#                         "product_id": "2",
#                         "product_price": 127.21,
#                         "product_quantity": 1
#                     }

#                 ],
#                 "total_price": 12,
#                 "payment_details": {
#                     "payment_method": "CREDIT_CARD",
#                     "card_number": "123456789012345",
#                     "expiration_year": 2022,
#                     "expiration_month": 3,
#                     "cvv": "123",
#                     "card_type": "VISA"
#                 }
#             }
#         ),
#         content_type="application/json",
#     )

#     data = json.loads(resp.data)
#     assert resp.status_code == 201
#     assert purchase_order.purchase_order_id == data["purchase_order_id"]
#     assert purchase_order.cvv == data["cvv"]
#     assert purchase_order.comments == data["comments"]
#     assert purchase_order.expiration_month == data["expiration_month"]
#     assert purchase_order.expiration_year == data["expiration_year"]
#     assert purchase_order.card_number == data["card_number"]
#     assert purchase_order.total_price == data["total_price"]
#     assert purchase_order.user_id == data["user_id"]
#     assert "products" in data


# def test_get_purchase_order_by_user_id(test_client, test_database):
#     test_database.session.add(purchase_order)
#     test_database.session.commit()

#     resp = test_client.get("/purchase-orders/1")

#     data = json.loads(resp.data)
#     assert resp.status_code == 200
#     assert purchase_order.purchase_order_id == data[0]["purchase_order_id"]
#     assert purchase_order.cvv == data[0]["cvv"]
#     assert purchase_order.comments == data[0]["comments"]
#     assert purchase_order.expiration_month == data[0]["expiration_month"]
#     assert purchase_order.expiration_year == data[0]["expiration_year"]
#     assert purchase_order.card_number == data[0]["card_number"]
#     assert purchase_order.total_price == data[0]["total_price"]
#     assert purchase_order.user_id == data[0]["user_id"]
#     assert "products" in data[0]

def test_get_no_existing_purchase_order_by_user_id(test_client, test_database):

    resp = test_client.get("/purchase-orders/1")

    data = json.loads(resp.data)
    assert resp.status_code == 404


