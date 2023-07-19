from src import create_app
from src import db

app = create_app()

with app.app_context():
    from src.api.models.reviews import Review

    db.create_all()
