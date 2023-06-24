from flask import Flask, jsonify, request, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

users_bp = Blueprint("users", __name__, url_prefix="/users")
    
user = os.getenv('POSTGRES_USER')
passwd = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')
host = os.getenv('POSTGRES_SERVICE')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{db}"
db = SQLAlchemy(app)

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        user = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 201


@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user))


@users_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    return f"Update user with id ${user_id}", 200


app.register_blueprint(users_bp)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify(users_schema.dump(users))

# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get_or_404(user_id)
#     return jsonify(user_schema.dump(user))

# @app.route('/users', methods=['POST'])
# def create_user():
#     try:
#         user = user_schema.load(request.json)
#     except ValidationError as e:
#         return jsonify(e.messages), 400
#     db.session.add(user)
#     db.session.commit()
#     return jsonify(user_schema.dump(user)), 201


if __name__ == "__main__":
    app.run(debug=True, host=os.environ["EXPOSED_INTERFACES"])
