from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.category_service import CategoryService
from src.api.interfaces.persistence.category_dao import CategoryDao
from src.api.services.category_service_impl import CategoryServiceImpl
from src.api.persistence.category_dao_impl import CategoryDaoImpl


def configure(binder):
    binder.bind(CategoryService, to=CategoryServiceImpl, scope=singleton)
    binder.bind(CategoryDao, to=CategoryDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_SERVICE')
    database = os.getenv('POSTGRES_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.category_controller import categories_bp

    app.register_blueprint(categories_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
