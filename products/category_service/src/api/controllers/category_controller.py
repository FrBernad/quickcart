from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.category_service import CategoryService
from src.api.schemas.requests.request_schema import (
    create_category_schema,
    update_category_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

categories_bp = Blueprint("main", __name__, url_prefix="/categories")


@inject
@categories_bp.route("", methods=["POST"])
@expects_json(create_category_schema)
def create_category(category_service: CategoryService):
    data = request.get_json()

    name = data.get("name")
    return f"Create category with name {name}", 201


@inject
@categories_bp.route("", methods=["GET"])
def get_categories(category_service: CategoryService):
    categories = [
        {"name": "Tecnología", "id": "123"},
        {"name": "Tecnología", "id": "123"},
        {"name": "Tecnología", "id": "123"},
        {"name": "Tecnología", "id": "123"},
    ]
    response = make_response(jsonify(categories))
    response.status_code = 201
    return response


@inject
@categories_bp.route("/<string:category_id>", methods=["PUT"])
@expects_json(update_category_schema)
def update_category(category_id, category_service: CategoryService):
    data = request.get_json()
    name = data.get("name")

    return f"Update category with id {category_id} with name {name}", 204


@categories_bp.errorhandler(400)
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
