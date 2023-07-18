from src.api.interfaces.persistence.product_dao import ProductDao
from src.api.models.product import Product
from src.api.models.tag import Tag
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class ProductDaoImpl(ProductDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_product(self, name, price, category_id, tags, stock):
        product = Product(name, category_id, name, stock, price)

        tags = [Tag(name=tag) for tag in tags]

        product.tags.extend(tags)

        self.db.session.add(product)
        self.db.session.add_all(tags)
        self.db.session.commit()

        return product

    def delete_product(self, product):
        pass

    def get_products(self):
        return Product.query.all()

    def get_product_by_id(self, product_id):
        return Product.query.filter_by(id=product_id).first()

    def update_product(self, product, name, price, category_id, tags):
        pass

    def update_product_score(self, product, score):
        product.score = score
        self.db.session.commit()

    def update_product_stock(self, product, stock):
        product.stock = stock
        self.db.session.commit()

    # def get_user_by_id(self, user_id):
    #     return User.query.filter_by(id=user_id).first()

    # def get_user_by_email(self, email):
    #     return User.query.filter_by(email=email).first()

    # def create_user(self, username, email, password):
    #     user = User(username=username, email=email, password=password)
    #     self.db.session.add(user)
    #     self.db.session.commit()
    #     return user

    # def update_user(self, user, username, password):
    #     user.username = username
    #     user.password = password
    #     self.db.session.commit()
    #     return user
