from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.user_service import UserService
from src.api.interfaces.persistence.user_dao import UserDao
from src.api.services.user_service_impl import UserServiceImpl 
from src.api.persistence.user_dao_impl import UserDaoImpl

def configure(binder):
    binder.bind(UserService, to=UserServiceImpl, scope=singleton)
    binder.bind(UserDao, to=UserDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)
    
def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    database = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_SERVICE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.user_controller import users_bp  

    app.register_blueprint(users_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
