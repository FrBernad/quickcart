from src import create_app
from src import db

app = create_app()

with app.app_context():
    from src.api.models.shopping_cart import ShoppingCarts
    db.create_all()