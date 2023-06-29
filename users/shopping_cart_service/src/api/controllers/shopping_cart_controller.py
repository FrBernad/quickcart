from flask import jsonify, request, Blueprint, make_response
from src.api.schemas.requests.request_schema import update_shopping_cart_schema, checkout_shopping_cart_schema
from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from flask_expects_json import expects_json
from injector import inject
from jsonschema import ValidationError

shopping_cart_bp = Blueprint("shopping_cart", __name__, url_prefix="/shopping-cart")


@inject
@shopping_cart_bp.route("/<user_id>", methods=["GET"])
def get_shopping_cart_products(user_id, shopping_cart_service: ShoppingCartService):
    # Debería hacer un request al user service para chequear que exista el usuario
    user = shopping_cart_service.get_user_by_id(user_id)

    if not user:
        return jsonify({'message': f'User with id {user_id} not found'}), 404

    shopping_cart = shopping_cart_service.get_shopping_cart_by_user_id(user_id=user_id)

    if not shopping_cart:
        return jsonify([]), 200

    return f"Returning all the products in the shopping cart of the user {user_id}", 200


@inject
@expects_json(update_shopping_cart_schema)
@shopping_cart_bp.route("/<user_id>/<product_id>", methods=["PUT"])
def update_product_quantity_from_shopping_cart(user_id, product_id, shopping_cart_service: ShoppingCartService):
    # FIXME: Debería hacer un request al user service para chequear que exista el usuario

    user = shopping_cart_service.get_user_by_id(user_id=user_id)

    if not user:
        return jsonify({'message': f'User with id {user_id} not found'}), 404

    data = request.get_json()
    quantity = data.get('quantity')

    # FIXME: Debería hacer un request para ver que exista el producto
    product = shopping_cart_service.get_product_by_id(product_id=product_id)

    if not product:
        return jsonify({'message': f'Product with id {product_id} not found'}), 404

    shopping_cart_service.add_product(user_id=user_id, product_id=product_id, quantity=quantity)

    return make_response('', 204)


@inject
@expects_json(checkout_shopping_cart_schema)
@shopping_cart_bp.route("/<user_id>/checkout", methods=["POST"])
def checkout_shopping_cart(user_id, shopping_cart_service: ShoppingCartService):
    # FIXME: Debería hacer un request al user service para chequear que exista el usuario

    user = shopping_cart_service.get_user_by_id(user_id)
    shopping_cart_service.checkout_shopping_cart(user_id)

    return f"Checkout shopping cart from user with id {user_id}", 200


@inject
@shopping_cart_bp.route("/<user_id>/<product_id>", methods=["DELETE"])
def delete_product_from_shopping_cart(user_id, product_id, shopping_cart_service: ShoppingCartService):
    shopping_cart_service.delete_product_from_shopping_cart(user_id=user_id, product_id=product_id)
    return make_response('', 204)


@inject
@shopping_cart_bp.route("/user_id", methods=["DELETE"])
def delete_shopping_cart(user_id, shopping_cart_service: ShoppingCartService):
    shopping_cart_service.delete_shopping_cart(user_id=user_id)
    return make_response('', 204)


@shopping_cart_bp.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify(
            {'message': original_error.message,
             'error': 'Invalid input'}, ), 400)

    return error
