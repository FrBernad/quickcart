from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.schemas.requests.request_schema import (
    create_purchase_order_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

purchase_orders_bp = Blueprint(
    "purchase_orders", __name__, url_prefix="/purchase-orders"
)


@inject
@purchase_orders_bp.route("", methods=["POST"])
@expects_json(create_purchase_order_schema)
def create_purchase_order(purchase_order_service: PurchaseOrderService):
    return "Create purchase order", 201


@inject
@purchase_orders_bp.route("", methods=["GET"])
def get_purchase_orders(purchase_order_service: PurchaseOrderService):
    return jsonify({}), 200


@inject
@purchase_orders_bp.route("/<order_id>", methods=["GET"])
def get_purchase_order(order_id, purchase_order_service: PurchaseOrderService):
    return f"Get purchase order with id ${order_id}", 200


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
