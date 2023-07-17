from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.schemas.requests.request_schema import (
    create_purchase_order_schema,
)
from src.api.schemas.purchase_order_schema import (
    purchase_order_schema,
    purchase_orders_schema
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.api.models.products import Product
from src.api.models.payment_details import PaymentDetails
from src.api.models.card_type import CardType
from src.api.models.payment_method import PaymentMethod

purchase_orders_bp = Blueprint(
    "purchase_orders", __name__, url_prefix="/purchase-orders"
)


@inject
@purchase_orders_bp.route("", methods=["POST"])
@expects_json(create_purchase_order_schema)
def create_purchase_order(purchase_order_service: PurchaseOrderService):
    data = request.get_json()

    comments = data.get("comments")
    user_id = data.get("user_id")
    total_price = data.get('total_price')

    products_array = data.get("products", [])

    if len(products_array) == 0:
        return jsonify({}), 400

    products = []
    for p in products_array:
        products.append(
            Product(product_id=p.get('product_id'),
                    price=p.get('product_price'),
                    quantity=p.get('product_quantity'))
        )

    payment_details_obj = data.get('payment_details', {})
    if not payment_details_obj:
        return 'Payment details are missing or empty'

    card_type = getattr(CardType, data.get('card_type'), None)
    payment_method = getattr(PaymentMethod, data.get('payment_method'), None)

    payment_details = PaymentDetails(
        payment_method=payment_method,
        card_number=data.get('card_number'),
        expiration_year=data.get('expiration_year'),
        expiration_month=data.get('expiration_month'),
        cvv=data.get('cvv'),
        card_type=card_type
    )

    purchase_order = purchase_order_service.create_purchase_order(
        comments=comments,
        user_id=user_id,
        total_price=total_price,
        products=products,
        payment_details=payment_details
    )

    return jsonify(purchase_order_schema.dump(purchase_order)), 201


@inject
@purchase_orders_bp.route("", methods=["GET"])
def get_purchase_orders(purchase_order_service: PurchaseOrderService):
    purchase_order = purchase_order_service.get_purchase_orders()
    return jsonify(purchase_orders_schema.dump(purchase_order)), 200


@inject
@purchase_orders_bp.route("/<order_id>", methods=["GET"])
def get_purchase_order(purchase_order_id, purchase_order_service: PurchaseOrderService):
    purchase_order = purchase_order_service.get_purchase_order_by_id(purchase_order_id)
    return jsonify(purchase_order_schema.dump(purchase_order)),


@purchase_orders_bp.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(
            jsonify(
                {
                    "message": original_error.message,
                    "error": "Invalid input",
                },
            ),
            400,
        )

    return error
