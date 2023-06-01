from flask import Flask, jsonify, request, Blueprint

app = Flask(__name__)

tags_bp = Blueprint("tags", __name__, url_prefix="/tags")


@tags_bp.route("/", methods=["GET"])
def get_tags():
    return "Get tags", 200


@tags_bp.route("/", methods=["POST"])
def create_tag():
    return "Create tag", 200


@tags_bp.route("/<tag_name>", methods=["DELETE"])
def delete_tag(tag_name):
    return f"Delete tag with name ${tag_name}", 200


app.register_blueprint(tags_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
