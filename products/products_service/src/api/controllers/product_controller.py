from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.product_service import ProductService
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

    name = data.get("name")
    price = data.get("price")
    category_id = data.get("category_id")
    tags = data.get("tags")
    stock = data.get("stock")

    # TODO: Check category is valid
    product = product_service.create_product(name, price, category_id, tags, stock)

    return jsonify(product_schema.dump(product)), 201


@inject
@products_bp.route("/", methods=["GET"])
def get_products(product_service: ProductService):
    products = product_service.get_products()

    return jsonify(products_schema.dump(products)), 200


@inject
@products_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    if not product:
        return jsonify({"message": f"Product with id {product_id} not found"}), 404

    return jsonify(product_schema.dump(product)), 200


@inject
@expects_json(update_product_schema)
@products_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    if not product:
        return jsonify({"message": f"Product with id {product_id} not found"}), 404

    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    category_id = data.get("category_id")
    tags = data.get("tags")

    product_service.update_product(product, name, price, category_id, tags)

    return "", 204


@inject
@products_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    if not product:
        return jsonify({"message": f"Product with id {product_id} not found"}), 404

    product_service.delete_product(product)

    return "", 204


@inject
@expects_json(update_product_score_schema)
@products_bp.route("/<product_id>/score", methods=["PUT"])
def update_product_score(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    if not product:
        return jsonify({"message": f"Product with id {product_id} not found"}), 404

    data = request.get_json()

    score = data.get("score")

    product_service.update_product(product, score)

    return "", 204


@inject
@expects_json(update_product_stock_schema)
@products_bp.route("/<product_id>/stock", methods=["PUT"])
def update_product_stock(product_id, product_service: ProductService):
    product = product_service.get_product_by_id(product_id)

    if not product:
        return jsonify({"message": f"Product with id {product_id} not found"}), 404

    data = request.get_json()

    stock = data.get("stock")

    product_service.update_product(product, stock)

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
