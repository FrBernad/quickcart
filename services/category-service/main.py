from flask import Flask, jsonify, request, make_response, Blueprint

app = Flask(__name__)

categories_bp = Blueprint("main", __name__, url_prefix="/categories")

@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = [ 
        {"name":'Tecnología',"id":'123'},
    {"name":'Tecnología',"id":'123'},
     {"name":'Tecnología',"id":'123'},
    {"name":'Tecnología',"id":'123'}
    ]
    response = make_response(jsonify(categories))
    response.status_code = 201
    return response

@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    if "name" not in data:
      return jsonify({"error": "Field 'name' is required"}), 400
    category = {
        'name': data['name'],
    }
    return f"Create category with name ${category['name']}",200

@categories_bp.route('/<string:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    if "name" not in data:
      return jsonify({"error": "Field 'name' is required"}), 400
    category = {
        'name': data['name'],
    }
    return f"Update category with id {category_id} with name ${category['name']}",204

app.register_blueprint(categories_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
