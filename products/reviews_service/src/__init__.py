from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.review_service import ReviewService
from src.api.interfaces.persistence.review_dao import ReviewDao
from src.api.services.review_service_impl import ReviewServiceImpl
from src.api.persistence.review_dao_impl import ReviewDaoImpl


def configure(binder):
    binder.bind(ReviewService, to=ReviewServiceImpl, scope=singleton)
    binder.bind(ReviewDao, to=ReviewDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_SERVICE')
    database = os.getenv('POSTGRES_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.review_controller import reviews_bp

    app.register_blueprint(reviews_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
