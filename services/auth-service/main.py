from flask import Flask, jsonify, request, make_response, Blueprint

app = Flask(__name__)

auth_bp = Blueprint("main", __name__, url_prefix="/auth")

@auth_bp.route('/login', methods=['GET'])
def login():
    data = request.json
   
    if "email" not in data:
      return jsonify({"error": "Field 'email' is required"}), 400
    if "password" not in data:
      return jsonify({"error": "Field 'password' is required"}), 400
    return f"User with email {data['email']} and password {data['password']} login",200

@auth_bp.route('/refresh-token', methods=['POST'])
def refresh_token():
    return f"Refresh token",200

@auth_bp.route('/refresh-token', methods=['DELETE'])
def invalidate_session():
    return f"Invalidate session from user",200

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
