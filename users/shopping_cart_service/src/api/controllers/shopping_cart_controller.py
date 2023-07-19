from flask import jsonify, request, Blueprint, make_response
from src.api.schemas.requests.request_schema import (
    update_shopping_cart_schema,
    checkout_shopping_cart_schema,
)
from src.api.schemas.shopping_cart_product_schema import (
    shopping_cart_product_schema,
    shopping_cart_products_schema,
)
from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from flask_expects_json import expects_json
from injector import inject
from jsonschema import ValidationError
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException

from src.api.models.payment_info import PaymentInfo

shopping_cart_bp = Blueprint("shopping_cart", __name__, url_prefix="/shopping-cart")


@inject
@shopping_cart_bp.route("/<user_id>", methods=["GET"])
def get_shopping_cart_products(user_id, shopping_cart_service: ShoppingCartService):
    shopping_cart_products = shopping_cart_service.get_products(user_id=user_id)

    if len(shopping_cart_products) == 0:
        return "", 204

    return shopping_cart_products_schema.dump(shopping_cart_products), 200


@inject
@shopping_cart_bp.route("/<user_id>/<product_id>", methods=["PUT"])
@expects_json(update_shopping_cart_schema)
def update_shopping_cart_product_quantity(
        user_id, product_id, shopping_cart_service: ShoppingCartService
):
    data = request.get_json()
    quantity = data.get("quantity")

    shopping_cart_service.add_product(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
    )

    return "", 204


@inject
@shopping_cart_bp.route("/<user_id>/checkout", methods=["POST"])
@expects_json(checkout_shopping_cart_schema)
def checkout_shopping_cart(user_id, shopping_cart_service: ShoppingCartService):
    data = request.get_json()

    comments = data.get("comments")

    payment_info = PaymentInfo(
        payment_method=data['payment_method'],
        expiration_year=data['expiration_year'],
        expiration_month=data['expiration_month'],
        card_number=data['card_number'],
        cvv=data['cvv'],
        card_type=data['card_type'],
    )

    shopping_cart_service.checkout(user_id, payment_info, comments)

    return f"Checkout shopping cart for user with id {user_id}", 200


@inject
@shopping_cart_bp.route("/<user_id>/<product_id>", methods=["DELETE"])
def delete_shopping_cart_product(
        user_id,
        product_id,
        shopping_cart_service: ShoppingCartService,
):
    shopping_cart_service.delete_product(user_id=user_id, product_id=product_id)
    return "", 204


@inject
@shopping_cart_bp.route("/<user_id>", methods=["DELETE"])
def empty_shopping_cart(user_id, shopping_cart_service: ShoppingCartService):
    shopping_cart_service.empty(user_id=user_id)
    return "", 204


@shopping_cart_bp.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return {"message": original_error.message, "error": "Invalid input"}, 400

    return error


@shopping_cart_bp.errorhandler(GenericApiException)
def generic_api_exception(e):
    return jsonify(e.to_dict()), e.status_code
