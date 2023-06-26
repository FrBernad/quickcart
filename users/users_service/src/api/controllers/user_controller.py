
from flask import jsonify, request, Blueprint,make_response
from injector import inject
from src.api.schemas.users_schema import user_schema
from src.api.interfaces.services.user_service import UserService
from src.api.schemas.requests.request_schema import create_user_schema,update_user_schema
from flask_expects_json import expects_json
from jsonschema import ValidationError

users_bp = Blueprint("users", __name__, url_prefix="/users")

@inject
@users_bp.route("", methods=["POST"])
@expects_json(create_user_schema)
def create_user(userService: UserService):
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = userService.get_user_by_email(email)

    if user:
        return jsonify({'message': 'The email is already in use'}), 400
        
    new_user = userService.create_user(username, email, password)


    return jsonify({}), 201


@inject
@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id,  userService: UserService):
    user = userService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': f'User with id not found'}), 404
    
    return jsonify(user_schema.dump(user))

@inject
@expects_json(update_user_schema)
@users_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id,  userService: UserService):
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = userService.get_user_by_id(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user = userService.update_user(user, username, password)
            
    return jsonify({}), 204
    


@users_bp.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify(
            {'message': original_error.message},
            {'error':'Invalid input'}),400)
    # handle other "Bad Request"-errors
    return error
   