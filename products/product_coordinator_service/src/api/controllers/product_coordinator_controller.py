from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.schemas.users_schema import user_schema
from src.api.interfaces.services.product_coordinator_service import ProductCoordinatorService
from src.api.schemas.requests.request_schema import (
    create_product_schema,
    update_product_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

product_coordinator_bp = Blueprint(
    "product_coordinator", __name__, url_prefix="/product_coordinator"
)


@inject
@product_coordinator_bp.route("", methods=["POST"])
@expects_json(create_product_schema)
def create_product(product_coordinator_service: ProductCoordinatorService):
    return "Create product", 200


@inject
@product_coordinator_bp.route("/<product_id>", methods=["PUT"])
@expects_json(update_product_schema)
def update_product(product_id, product_coordinator_service: ProductCoordinatorService):
    return f"Update product with id ${product_id}", 200


@inject
@product_coordinator_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id, product_coordinator_service: ProductCoordinatorService):
    return f"Delete product with id ${product_id}", 200


@product_coordinator_bp.errorhandler(400)
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
