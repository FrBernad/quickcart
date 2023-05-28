from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.route("/<product_id>/reviews", methods=["POST"])
def create_review(product_id):
    return f"Create review for product with id ${product_id}", 200


@products_bp.route("/<product_id>/reviews", methods=["GET"])
def get_reviews(product_id):
    return f"Get reviews for product with id ${product_id}", 200


@reviews_bp.route("/<review_id>", methods=["GET"])
def get_review(review_id):
    return f"Get review with id ${review_id}", 200


app.register_blueprint(reviews_bp)
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
