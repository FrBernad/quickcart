from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.schemas.reviews_schema import reviews_schema
from src.api.interfaces.services.review_service import ReviewService
from src.api.schemas.requests.request_schema import (
    create_review_schema,
)
from flask_expects_json import expects_json
from jsonschema import ValidationError
from src.api.interfaces.exceptions.generic_api_exception import GenericApiException

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

@inject
@expects_json(create_review_schema)
@reviews_bp.route("/<product_id>", methods=["POST"])
def create_review(product_id, review_service: ReviewService):
    data = request.get_json()

    user_id = data.get("user_id")
    review_body = data.get("description")
    score = data.get("score")

    new_review = review_service.create_review(product_id, user_id, review_body, score)

    return jsonify(reviews_schema.dump(new_review)), 201


# /reviews?product-id=
@inject
@reviews_bp.route("", methods=["GET"])
def get_reviews_by_product(review_service: ReviewService):
    
    product_id = request.args.get('product-id')

    if product_id == None:
        return (
            jsonify({"message": f"query parameter product-id needed"}),
            400,
        )

    reviews = review_service.get_reviews_by_product(product_id=product_id)

    if not reviews:
        return (
            jsonify({"message": f"Reviews for product id {product_id} not found"}),
            404,
        )

    return jsonify(reviews_schema.dump(reviews)), 200


# @inject
# @reviews_bp.route("/<review_id>", methods=["GET"])
# def get_review_by_id(review_id, review_service: ReviewService):
#     review = review_service.get_review_by_id(review_id=review_id)

#     if not review:
#         return jsonify({"message": f"Review with id {review_id} not found"}), 404

#     return jsonify(reviews_schema.dump(review)), 200

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


@reviews_bp.errorhandler(GenericApiException)
def generic_api_exception(e):
    return jsonify(e.to_dict()), e.status_code
