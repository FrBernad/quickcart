from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
        
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    database = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_SERVICE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.users_bp import users_bp  

    app.register_blueprint(users_bp)

    return app
