
from flask import jsonify, request, Blueprint
from src.api.schemas.users_schema import user_schema
from src.api.cruds.users import (  # isort:skip
    get_user_by_email,
    add_user,
    get_user_by_id,
    update_user,
)


users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')


    if not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = get_user_by_email(email)

    if user:
        return jsonify({'message': 'The email is already in use'}), 400
        
    new_user = add_user(username, email, password)

    return jsonify({'id': new_user.id, 'name': new_user.username, 'email': new_user.email}), 201


@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user_schema.dump(user))


@users_bp.route("/<user_id>", methods=["PUT"])
def put(user_id):
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')


    if not username or not email:
        return jsonify({'message': 'Missing required fields'}), 400

    user = get_user_by_id(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user = update_user(user, username, email)
            

    return f"Update user with id ${user.id}", 200
