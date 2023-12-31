from abc import ABC, abstractmethod


class ProductDao(ABC):
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
    def delete_product(self, product_id):
        pass

    @abstractmethod
    def update_product(self, product, name, price, category_id, tags):
        pass

    @abstractmethod
    def update_product_score(self, product, score):
        pass

    @abstractmethod
    def update_product_stock(self, product, stock):
        pass
