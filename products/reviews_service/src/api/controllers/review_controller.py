from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.review_service import ReviewService
from src.api.schemas.requests.request_schema import (
    create_review_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")
products_bp = Blueprint("products", __name__, url_prefix="/products")


@inject
@expects_json(create_review_schema)
@products_bp.route("/<product_id>/reviews", methods=["POST"])
def create_review(product_id, review_service: ReviewService):
    return f"Create review for product with id ${product_id}", 201


@inject
@products_bp.route("/<product_id>/reviews", methods=["GET"])
def get_reviews_by_product(product_id, review_service: ReviewService):
    return f"Get reviews for product with id ${product_id}", 200


@inject
@reviews_bp.route("/<review_id>", methods=["GET"])
def get_review_by_id(review_id, review_service: ReviewService):
    return f"Get review with id ${review_id}", 200


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


@reviews_bp.errorhandler(400)
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
