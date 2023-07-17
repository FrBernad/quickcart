from abc import ABC, abstractmethod


class PurchaseOrderService(ABC):

    @abstractmethod
    def get_purchase_orders(self):
        pass

    @abstractmethod
    def get_purchase_order_by_id(self, purchase_order_id):
        pass

    @abstractmethod
    def create_purchase_order(self, comments,
                              user_id,
                              total_price,
                              products,
                              payment_details):
        pass
