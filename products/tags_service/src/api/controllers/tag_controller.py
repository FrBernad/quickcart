from flask import jsonify, request, Blueprint, make_response
from injector import inject
from src.api.interfaces.services.user_service import TagService
from src.api.schemas.requests.request_schema import (
    create_tag_schema,
)
from src.api.schemas.tag_schema import (
    tags_schema,
    tag_schema
)
from flask_expects_json import expects_json
from jsonschema import ValidationError

tags_bp = Blueprint("tags", __name__, url_prefix="/tags")


@inject
@tags_bp.route("", methods=["POST"])
@expects_json(create_tag_schema)
def create_tag(tag_service: TagService):
    data = request.get_json()
    name = data.get('name')
    tag = tag_service.create_tag(tag_name=name)

    return jsonify(tag_schema.dump(tag)), 201


@inject
@tags_bp.route("", methods=["GET"])
def get_tags(tag_service: TagService):
    tags = tag_service.get_tags()

    return jsonify(tags_schema.dump(tags)), 200


@inject
@tags_bp.route("/<tag_name>", methods=["DELETE"])
def delete_tag(tag_name, tag_service: TagService):
    tag = tag_service.delete_tag(tag_name)
    return jsonify({}), 204


@tags_bp.errorhandler(400)
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
