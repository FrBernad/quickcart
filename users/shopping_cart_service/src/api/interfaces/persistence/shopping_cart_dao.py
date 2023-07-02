from abc import ABC, abstractmethod


class ShoppingCartDao(ABC):
    @abstractmethod
    def get_products(self, user_id):
        pass

    @abstractmethod
    def add_product(self, user_id, product_id, quantity):
        pass

    @abstractmethod
    def delete_product(self, user_id, product_id):
        pass

    @abstractmethod
    def empty(self, user_id):
        pass
