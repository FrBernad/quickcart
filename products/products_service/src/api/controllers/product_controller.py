from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.schemas.users_schema import product_schema
from src.api.interfaces.services.product_service import ProductService
from src.api.schemas.requests.request_schema import (
    create_product_schema,
    update_product_schema,
    update_product_score_schema,
    update_product_stock_schema
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

products_bp = Blueprint("products", __name__, url_prefix="/products")


@inject
@products_bp.route("", methods=["POST"])
@expects_json(create_product_schema)
def create_product(product_service: ProductService):
    data = request.get_json()
    return "Create product", 201


@inject
@products_bp.route("/", methods=["GET"])
def get_products(product_service: ProductService):
    return "Get products", 200


@inject
@products_bp.route("/<product_id>", methods=["GET"])
def get_product_by_id(product_id, product_service: ProductService):
    return f"Get product with id ${product_id}", 200


@inject
@expects_json(update_product_schema)
@products_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id, product_service: ProductService):
    return f"Update product with id ${product_id}", 200


@inject
@products_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id, product_service: ProductService):
    return f"Delete product with id ${product_id}", 200


@inject
@expects_json(update_product_score_schema)
@products_bp.route("/<product_id>/score", methods=["PUT"])
def update_product_score(product_id, product_service: ProductService):
    return f"Update product with id ${product_id} score", 200


@inject
@expects_json(update_product_stock_schema)
@products_bp.route("/<product_id>/stock", methods=["PUT"])
def update_product_stock(product_id, product_service: ProductService):
    return f"Update product with id ${product_id} stock", 200


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
