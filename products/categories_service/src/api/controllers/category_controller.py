from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.category_service import CategoryService
from src.api.schemas.requests.request_schema import (
    create_category_schema,
    update_category_schema,
)
from src.api.schemas.category_schema import categories_schema, category_schema
from flask_expects_json import expects_json
from jsonschema import ValidationError
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException

categories_bp = Blueprint("main", __name__, url_prefix="/categories")


@inject
@categories_bp.route("", methods=["POST"])
@expects_json(create_category_schema)
def create_category(category_service: CategoryService):
    data = request.get_json()
    name = data.get("name")
    category = category_service.create_category(name=name)

    return jsonify(category_schema.dump(category)), 201


@inject
@categories_bp.route("", methods=["GET"])
def get_categories(category_service: CategoryService):
    categories = category_service.get_categories()
    return jsonify(categories_schema.dump(categories)), 200


@inject
@categories_bp.route("/<category_id>", methods=["PUT"])
@expects_json(update_category_schema)
def update_category(category_id, category_service: CategoryService):
    data = request.get_json()
    name = data.get("name")
    category_service.update_category(category_id=category_id, name=name)
    return jsonify({}), 204


@inject
@categories_bp.route("/<category_id>", methods=["GET"])
def get_category_by_id(category_id, category_service: CategoryService):
    category = category_service.get_category_by_id(category_id=category_id)
    return jsonify(category_schema.dump(category)), 200


@categories_bp.errorhandler(404)
def not_found(error):
    return jsonify({"message": f"url {request.url} not found"}), 404


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


@categories_bp.errorhandler(GenericApiException)
def generic_api_exception(e):
    return jsonify(e.to_dict()), e.status_code
