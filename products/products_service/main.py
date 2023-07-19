from src import create_app
from src import db

app = create_app()

with app.app_context():
    from src.api.models.product import Product
    from src.api.models.tag import Tag
    db.create_all()