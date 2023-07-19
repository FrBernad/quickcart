from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.product_service import ProductService
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException
from src.api.schemas.requests.request_schema import (
    create_product_schema,
    update_product_schema,
    update_product_score_schema,
    update_product_stock_schema,
)
from src.api.schemas.products_schema import (
    product_schema,
    products_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError


products_bp = Blueprint("products", __name__, url_prefix="/products")


@inject
@products_bp.route("", methods=["POST"])
@expects_json(create_product_schema)
def create_product(product_service: ProductService):
    data = request.get_json()

    user_id = data.get("user_id")
    name = data.get("name")
    price = data.get("price")
    category_id = data.get("category_id")
    tags = data.get("tags")
    stock = data.get("stock")

    product = product_service.create_product(
        user_id, name, price, category_id, tags, stock
    )

    return jsonify(product_schema.dump(product)), 201


@inject
@products_bp.route("", methods=["GET"])
def get_products(product_service: ProductService):
    products = product_service.get_products()
    if not products:
        "", 204

    return jsonify(products_schema.dump(products)), 200


@inject
@products_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    return jsonify(product_schema.dump(product)), 200


@inject
@expects_json(update_product_schema)
@products_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id, product_service: ProductService):
    data = request.get_json()

    user_id = data.get("user_id")
    name = data.get("name")
    price = data.get("price")
    category_id = data.get("category_id")
    tags = data.get("tags")

    product_service.update_product(user_id, product_id, name, price, category_id, tags)

    return "", 204


@inject
@products_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id, product_service: ProductService):
    product_service.delete_product(product_id)

    return "", 204


@inject
@expects_json(update_product_score_schema)
@products_bp.route("/<product_id>/score", methods=["PUT"])
def update_product_score(product_id, product_service: ProductService):
    data = request.get_json()

    score = data.get("score")

    product_service.update_product(product_id, score)

    return "", 204


@inject
@expects_json(update_product_stock_schema)
@products_bp.route("/<product_id>/stock", methods=["PUT"])
def update_product_stock(product_id, product_service: ProductService):
    data = request.get_json()

    stock = data.get("stock")

    product_service.update_product(product_id, stock)

    return "", 204


@products_bp.errorhandler(400)
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


@products_bp.errorhandler(GenericApiException)
def generic_api_exception(e):
    return jsonify(e.to_dict()), e.status_code
