from flask import Flask, jsonify, request, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError


def create_app():
        
    app = Flask(__name__)

    users_bp = Blueprint("users", __name__, url_prefix="/users")
        
    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_SERVICE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{db}"
    db = SQLAlchemy(app)

    class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        email = db.Column(db.String(50), unique=True)

        def __init__(self, name, email):
            self.name = name
            self.email = email

    class UserSchema(Schema):
        name = fields.Str(required=True)
        email = fields.Email(required=True)

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    @users_bp.route("", methods=["POST"])
    def create_user():
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({'message': 'Missing required fields'}), 400

        # Create a new user object
        new_user = User(name=name, email=email)

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201


    @users_bp.route("/<user_id>", methods=["GET"])
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user))


    @users_bp.route("/<user_id>", methods=["PUT"])
    def update_user(user_id):
        return f"Update user with id ${user_id}", 200

    app.register_blueprint(users_bp)

    return app

if __name__ == "__main__": 
    app = create_app()
    app.run(debug=True, host=os.environ["EXPOSED_INTERFACES"])
