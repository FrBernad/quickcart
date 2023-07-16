from abc import ABC, abstractmethod


class PurchaseOrderDao(ABC):

    @abstractmethod
    def get_purchase_orders(self, email):
        pass

    @abstractmethod
    def get_purchase_order_by_id(self, email):
        pass

    @abstractmethod
    def get_purchase_order_by_user_id(self, user, username, password):
        pass

    @abstractmethod
    def create_purchase_order(self, username, email, password):
        pass
