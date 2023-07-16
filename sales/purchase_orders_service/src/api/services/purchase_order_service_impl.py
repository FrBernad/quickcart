from src.api.interfaces.services.user_service import PurchaseOrderService
from src.api.interfaces.persistence.user_dao import PurchaseOrderDao
from injector import inject


class PurchaseOrderServiceImpl(PurchaseOrderService):

    @inject
    def __init__(self, purchase_order_dao: PurchaseOrderDao):
        self.purchase_order_dao = purchase_order_dao

    def get_user_by_email(self, email):
        return self.purchase_order_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        return self.purchase_order_dao.get_user_by_id(user_id=user_id)

    def create_user(self, username, email, password):
        return self.purchase_order_dao.create_user(username=username, email=email, password=password)

    def update_user(self, user, username, password):
        return self.purchase_order_dao.update_user(user=user, username=username, password=password)

    def get_purchase_orders(self, email):
        return self.purchase_order_dao.get_purchase_orders(email=email)

    def get_purchase_order_by_id(self, email):
        return self.purchase_order_dao.get_purchase_order_by_id(user_id=user_id)

    def get_purchase_order_by_user_id(self, user, username, password):
        pass

    def create_purchase_order(self, username, email, password):
        pass
