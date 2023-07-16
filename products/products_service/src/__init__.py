from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.product_service import ProductService
from src.api.interfaces.persistence.product_dao import ProductDao
from src.api.services.product_service_impl import ProductServiceImpl
from src.api.persistence.product_dao_impl import ProductDaoImpl


def configure(binder):
    binder.bind(ProductService, to=ProductServiceImpl, scope=singleton)
    binder.bind(ProductDao, to=ProductDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_SERVICE')
    database = os.getenv('POSTGRES_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.product_controller import products_bp

    app.register_blueprint(products_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
