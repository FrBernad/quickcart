from src.api.interfaces.services.purchase_order_service import PurchaseOrderService
from src.api.interfaces.persistence.purchase_order_dao import PurchaseOrderDao
from injector import inject


class PurchaseOrderServiceImpl(PurchaseOrderService):

    @inject
    def __init__(self, purchase_order_dao: PurchaseOrderDao):
        self.purchase_order_dao = purchase_order_dao

    def get_purchase_orders(self):
        return self.purchase_order_dao.get_purchase_orders()

    def get_purchase_order_by_user_id(self, user_id, product_id = None):
        return self.purchase_order_dao.get_purchase_order_by_user_id(user_id=user_id, product_id=product_id)

    def create_purchase_order(self, comments,
                              user_id,
                              total_price,
                              products,
                              payment_details):
        purchase_order = self.purchase_order_dao.create_purchase_order_with_products(comments=comments,
                                                                                     user_id=user_id,
                                                                                     total_price=total_price,
                                                                                     products=products,
                                                                                     payment_details=payment_details)
        return purchase_order
