from src.api.interfaces.persistence.purchase_order import PurchaseOrderDao
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
        pass

    def get_purchase_order_by_id(self, purchase_order_id):
        purchase_order = PurchaseOrders.query.filter_by(purchase_order_id=purchase_order_id).first()
        products = ProductsPurchased.query.filter_by(purchase_order_id=purchase_order_id).all()
        return PurchaseOrderDetails(comments=purchase_order.comments,
                                    user_id=purchase_order.user_id,
                                    total_price=purchase_order.total_price,
                                    payment_method=purchase_order.payment_details.payment_method,
                                    card_number=purchase_order.payment_details.card_number,
                                    expiration_year=purchase_order.payment_details.expiration_year,
                                    expiration_month=purchase_order.payment_details.expiration_month,
                                    cvv=purchase_order.payment_details.cvv,
                                    card_type=purchase_order.payment_details.card_type,
                                    products=products)

    def create_purchase_order(self, comments,
                              user_id,
                              total_price,
                              products,
                              payment_details):
        try:
            with self.db.session.begin_nested():
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
                self.db.session.flush()

                products_models = []
                for product in products:
                    p = ProductsPurchased(purchase_order_id=purchase_order.purchase_order_id,
                                          product_id=product.id,
                                          product_price=product.price,
                                          product_quantity=product.quantity)
                    products_models.append(p)
                    self.db.session.add(p)

            self.db.session.commit()

            return PurchaseOrderDetails(comments=comments,
                                        user_id=user_id,
                                        total_price=total_price,
                                        payment_method=payment_details.payment_method,
                                        card_number=payment_details.card_number,
                                        expiration_year=payment_details.expiration_year,
                                        expiration_month=payment_details.expiration_month,
                                        cvv=payment_details.cvv,
                                        card_type=payment_details.card_type,
                                        products=products_models)
        except Exception as e:
            # Rollback the transaction if any error occurs
            self.db.session.rollback()
            return None
