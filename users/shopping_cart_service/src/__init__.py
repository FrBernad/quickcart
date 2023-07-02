from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.shopping_cart_service import ShoppingCartService
from src.api.interfaces.persistence.shopping_cart_dao import ShoppingCartDao
from src.api.services.shopping_cart_service_impl import ShoppingCartServiceImpl
from src.api.persistence.shopping_cart_dao_impl import ShoppingCartDaoImpl


def configure(binder):
    binder.bind(ShoppingCartService, to=ShoppingCartServiceImpl, scope=singleton)
    binder.bind(ShoppingCartDao, to=ShoppingCartDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv("POSTGRES_USER")
    passwd = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_SERVICE")
    database = os.getenv("POSTGRES_DB")

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.shopping_cart_controller import shopping_cart_bp

    app.register_blueprint(shopping_cart_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
