from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50), unique=True)

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

# class UserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     email = fields.Email(required=True)

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

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


@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
