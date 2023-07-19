from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from injector import inject
from flask_sqlalchemy import SQLAlchemy
from src.api.models.purchase_orders import PurchaseOrders
from src.api.models.purchase_products import ProductsPurchased
from src.api.models.purchase_order_details import PurchaseOrderDetails


class PurchaseOrderDaoImpl(PurchaseOrderDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_purchase_orders(self):
        return PurchaseOrders.query.all()

    def get_purchase_order_by_id(self, purchase_order_id):

        purchase_order = PurchaseOrders.query.filter_by(purchase_order_id=purchase_order_id).first()
        return purchase_order

    def create_purchase_order_with_products(self, comments,
                                            user_id,
                                            total_price,
                                            products,
                                            payment_details):
        try:
            purchase_order = PurchaseOrders(comments=comments,
                                            user_id=user_id,
                                            total_price=total_price,
                                            payment_method=payment_details.payment_method,
                                            card_number=payment_details.card_number,
                                            expiration_year=payment_details.expiration_year,
                                            expiration_month=payment_details.expiration_month,
                                            cvv=payment_details.cvv,
                                            card_type=payment_details.card_type)
            self.db.session.add(purchase_order)

            for product in products:
                p = ProductsPurchased(purchase_order=purchase_order,
                                      product_id=product.id,
                                      product_price=product.price,
                                      product_quantity=product.quantity)
                self.db.session.add(p)
            self.db.session.commit()
            return purchase_order
        except Exception as e:
            self.db.session.rollback()
            return None
