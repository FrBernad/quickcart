from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def create_product(self, user_id, name, price, category_id, tags, stock):
        pass

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def delete_product(self, product):
        pass

    @abstractmethod
    def update_product(self, user_id, product_id, name, price, category_id, tags):
        pass

    @abstractmethod
    def update_product_score(self, product_id, score):
        pass

    @abstractmethod
    def update_product_stock(self, product_id, stock):
        pass
