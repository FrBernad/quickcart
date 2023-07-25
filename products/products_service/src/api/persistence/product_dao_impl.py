from src.api.interfaces.persistence.product_dao import ProductDao
from src.api.models.product import Product
from src.api.models.tag import Tag
from injector import inject
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound


class ProductDaoImpl(ProductDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_product(self, user_id, name, price, category_id, tags, stock):
        product = Product(
            user_id=user_id,
            name=name,
            category_id=category_id,
            stock=stock,
            price=price,
        )

        product.tags = self._get_and_generate_tags(tags)

        self.db.session.add(product)
        self.db.session.commit()

        return product

    def delete_product(self, product_id):
        self.db.session.execute(self.db.delete(Product).where(Product.id == product_id))
        self.db.session.commit()

    def get_products(self):
        return self.db.session.scalars(self.db.select(Product)).all()

    def get_product_by_id(self, product_id):
        return Product.query.filter_by(id=product_id).first()

    def update_product(self, product, name, price, category_id, tags):
        product.name = name
        product.price = price
        product.category_id = category_id
        product.tags = self._get_and_generate_tags(tags)
        self.db.session.commit()

    def update_product_score(self, product, score):
        product.score = score
        self.db.session.commit()

    def update_product_stock(self, product, stock):
        product.stock = stock
        self.db.session.commit()

    def _get_and_generate_tags(self, tags):
        existing_tags = self.db.session.scalars(
            self.db.select(Tag).where(Tag.name.in_(tags))
        ).all()

        existing_tags_names = [tag.name for tag in existing_tags]

        new_tags = [Tag(name=tag) for tag in tags if tag not in existing_tags_names]

        self.db.session.add_all(new_tags)

        new_tags.extend(existing_tags)

        return new_tags
