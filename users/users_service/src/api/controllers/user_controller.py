
from flask import jsonify, request, Blueprint
from injector import inject
from src.api.schemas.users_schema import user_schema
from src.api.interfaces.services.user_service import UserService
from src.api.schemas.requests.request_schema import create_user_schema
from flask_expects_json import expects_json

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

    return jsonify({'id': new_user.id, 'name': new_user.username, 'email': new_user.email}), 201


@inject
@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id,  userService: UserService):
    user = userService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user_schema.dump(user))

@inject
@users_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id,  userService: UserService):
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')


    if not username or not email:
        return jsonify({'message': 'Missing required fields'}), 400

    user = userService.get_user_by_id(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user = userService.update_user(user, username, email)
            

    return f"Update user with id ${user.id}", 200
