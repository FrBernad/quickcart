from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

purchase_orders_bp = Blueprint(
    "purchase_orders", __name__, url_prefix="/purchase_orders"
)


@purchase_orders_bp.route("/", methods=["POST"])
def create_purchase_order():
    return "Create purchase order", 200


@purchase_orders_bp.route("/", methods=["GET"])
def get_purchase_orders():
    return "Get purchase orders", 200


@purchase_orders_bp.route("/<order_id>", methods=["GET"])
def get_purchase_order(order_id):
    return f"Get purchase order with id ${order_id}", 200


app.register_blueprint(purchase_orders_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
