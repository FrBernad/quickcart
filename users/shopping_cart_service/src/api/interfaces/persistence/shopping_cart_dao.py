from abc import ABC, abstractmethod


class ShoppingCartDao(ABC):

    @abstractmethod
    def get_shopping_cart_by_user_id(self, user_id):
        pass

    @abstractmethod
    def add_product(self, user_id, product_id, quantity):
        pass

    @abstractmethod
    def delete_product_from_shopping_cart(self, user_id, product_id):
        pass

    @abstractmethod
    def delete_shopping_cart(self, user_id):
        pass
