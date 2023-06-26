from flask import Flask, jsonify, request, make_response, Blueprint

app = Flask(__name__)

shopping_cart_bp = Blueprint("main", __name__, url_prefix="/users")


@shopping_cart_bp.route("/<string:user_id>/shopping-cart", methods=["GET"])
def get_shopping_cart_products(user_id):
    return f"Returning all the products in the shopping cart of the user {user_id}", 200


@shopping_cart_bp.route(
    "/<string:user_id>/shopping-cart/<string:product_id>", methods=["PUT"]
)
def update_product_quantity_from_shopping_cart(user_id, product_id):
    data = request.json
    if "quantity" not in data:
        return jsonify({"error": "Field 'quantity' is required"}), 400
    quantity = data["quantity"]
    return (
        f"Update the shopping cart of the user with id {user_id}. The quantity of the product {product_id} is now ${quantity}",
        200,
    )


@shopping_cart_bp.route(
    "/<string:user_id>/shopping-cart/<string:product_id>", methods=["DELETE"]
)
def delete_product_from_shopping_cart(user_id, product_id):
    return (
        f"Deleting product with id {product_id} from the shopping cart of the user with id {user_id}",
        200,
    )

@shopping_cart_bp.route("/<string:user_id>/shopping-cart/checkout", methods=["POST"])
def checkout_shopping_cart(user_id):
    return f"Checkout shopping cart from user with id {user_id}", 200


@shopping_cart_bp.route("/<string:user_id>/shopping-cart", methods=["DELETE"])
def delete_shopping_cart(user_id):
    return f"Deleting shopping cart from user with id {user_id}", 200


app.register_blueprint(shopping_cart_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
