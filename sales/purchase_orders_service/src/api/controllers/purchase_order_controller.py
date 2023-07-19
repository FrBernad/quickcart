from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.schemas.requests.request_schema import (
    create_purchase_order_schema,
)
from src.api.schemas.purchase_order_schema import (
    purchase_order_schema,
    purchase_orders_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError
from src.api.models.product import Product
from src.api.models.payment_details import PaymentDetails
from src.api.models.card_type import CardType
from src.api.models.payment_method import PaymentMethod
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException

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
    total_price = data.get("total_price")

    products_array = data.get("products", [])

    if len(products_array) == 0:
        return (
            jsonify(
                {
                    "message": "Missing products",
                    "error": "Invalid input",
                }
            ),
            400,
        )

    products = []
    for p in products_array:
        products.append(
            Product(
                product_id=p.get("product_id"),
                price=p.get("product_price"),
                quantity=p.get("product_quantity"),
            )
        )

    payment_details_map = data.get("payment_details", {})
    if not payment_details_map:
        return (
            jsonify(
                {
                    "message": "Payment details are missing or empty",
                    "error": "Invalid input",
                }
            ),
            400,
        )

    card_type = getattr(CardType, payment_details_map.get("card_type"), None)
    payment_method = getattr(
        PaymentMethod, payment_details_map.get("payment_method"), None
    )

    payment_details = PaymentDetails(
        payment_method=payment_method,
        card_number=payment_details_map.get("card_number"),
        expiration_year=payment_details_map.get("expiration_year"),
        expiration_month=payment_details_map.get("expiration_month"),
        cvv=payment_details_map.get("cvv"),
        card_type=card_type,
    )

    purchase_order = purchase_order_service.create_purchase_order(
        comments=comments,
        user_id=user_id,
        total_price=total_price,
        products=products,
        payment_details=payment_details,
    )

    return jsonify(purchase_order_schema.dump(purchase_order)), 201


@inject
@purchase_orders_bp.route("", methods=["GET"])
def get_purchase_orders(purchase_order_service: PurchaseOrderService):
    purchase_order = purchase_order_service.get_purchase_orders()
    return jsonify(purchase_orders_schema.dump(purchase_order)), 200


@inject
@purchase_orders_bp.route("/<user_id>", methods=["GET"])
def get_purchase_order(user_id, purchase_order_service: PurchaseOrderService):
    product_id = request.args.get(
        "product-id"
    )  # Retrieve the product_id query parameter

    purchase_orders = purchase_order_service.get_purchase_order_by_user_id(
        user_id=user_id, product_id=product_id
    )

    if not purchase_orders:
        return jsonify(purchase_orders_schema.dump(purchase_orders)), 404
    return jsonify(purchase_orders_schema.dump(purchase_orders)), 200


@purchase_orders_bp.errorhandler(404)
def not_found(error):
    return jsonify({"message": f"url {request.url} not found"}), 404


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


@purchase_orders_bp.errorhandler(GenericApiException)
def generic_api_exception(e):
    return jsonify(e.to_dict()), e.status_code
