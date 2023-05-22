from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

product_coordinator_bp = Blueprint(
    "product_coordinator", __name__, url_prefix="/product_coordinator"
)


@product_coordinator_bp.route("/", methods=["POST"])
def create_product():
    return "Create product", 200


@product_coordinator_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id):
    return f"Update product with id ${product_id}", 200


@product_coordinator_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    return f"Delete product with id ${product_id}", 200


app.register_blueprint(product_coordinator_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
