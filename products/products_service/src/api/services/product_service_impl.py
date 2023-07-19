from src.api.interfaces.services.product_service import ProductService
from src.api.interfaces.persistence.product_dao import ProductDao
from injector import inject


class ProductServiceImpl(ProductService):
    @inject
    def __init__(self, product_dao: ProductDao):
        self.product_dao = product_dao

    def create_product(self, name, price, category_id, tags, stock):
        return self.product_dao.create_product(
            name=name, price=price, category_id=category_id, tags=tags, stock=stock
        )

    def get_products(self):
        return self.product_dao.get_products()

    def get_product_by_id(self, product_id):
        return self.product_dao.get_product_by_id(product_id)

    def delete_product(self, product):
        self.product_dao.delete_product(product)

    def update_product(self, product, name, price, category_id, tags):
        self.product_dao.update_product(
            product=product, name=name, price=price, category_id=category_id, tags=tags
        )

    def update_product_score(self, product, score):
        self.product_dao.update_product_score(product=product, score=score)

    def update_product_stock(self, product, stock):
        self.product_dao.update_product_stock(product=product, stock=stock)
