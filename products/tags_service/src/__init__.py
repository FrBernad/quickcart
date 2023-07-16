from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.tag_service import TagService
from src.api.interfaces.persistence.tag_dao import TagDao
from src.api.services.tag_service_impl import TagServiceImpl
from src.api.persistence.tag_dao_impl import TagDaoImpl


def configure(binder):
    binder.bind(TagService, to=TagServiceImpl, scope=singleton)
    binder.bind(TagDao, to=TagDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_SERVICE')
    database = os.getenv('POSTGRES_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.tag_controller import tags_bp

    app.register_blueprint(tags_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
