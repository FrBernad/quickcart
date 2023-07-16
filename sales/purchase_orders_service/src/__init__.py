from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import singleton
import os

from src.api.persistence.db import db
from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from src.api.services.purchase_order_service_impl import PurchaseOrderServiceImpl
from src.api.persistence.purchase_order_dao_impl import PurchaseOrderDaoImpl


def configure(binder):
    binder.bind(PurchaseOrderService, to=PurchaseOrderServiceImpl, scope=singleton)
    binder.bind(PurchaseOrderDao, to=PurchaseOrderDaoImpl, scope=singleton)
    binder.bind(SQLAlchemy, to=db, scope=singleton)


def create_app():
    app = Flask(__name__)

    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_SERVICE')
    database = os.getenv('POSTGRES_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}:5432/{database}"

    db.init_app(app)

    from src.api.controllers.purchase_order_controller import purchase_orders_bp

    app.register_blueprint(purchase_orders_bp)

    FlaskInjector(app=app, modules=[configure])

    return app
