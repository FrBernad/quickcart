from abc import ABC, abstractmethod


class ShoppingCartService(ABC):
    @abstractmethod
    def get_products(self, user_id):
        pass

    @abstractmethod
    def add_product(self, user_id, product_id, quantity):
        pass

    @abstractmethod
    def checkout(self, username, payment_info):
        pass

    @abstractmethod
    def delete_product(self, user_id, product_id):
        pass

    @abstractmethod
    def empty(self, user_id):
        pass
