from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.route("/", methods=["GET"])
def get_products():
    return "Get products", 200


@products_bp.route("/", methods=["POST"])
def create_product():
    return "Create product", 200


@products_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id):
    return f"Get product with id ${product_id}", 200


@products_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id):
    return f"Update product with id ${product_id}", 200


@products_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    return f"Delete product with id ${product_id}", 200


@products_bp.route("/<product_id>/score", methods=["PUT"])
def update_product_score(product_id):
    return f"Update product with id ${product_id} score", 200


@products_bp.route("/<product_id>/stock", methods=["PUT"])
def update_product_stock(product_id):
    return f"Update product with id ${product_id} stock", 200


app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
