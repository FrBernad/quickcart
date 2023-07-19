from src.api.interfaces.persistence.category_dao import CategoryDao
from src.api.models.categories import Category
from injector import inject
from flask_sqlalchemy import SQLAlchemy


class CategoryDaoImpl(CategoryDao):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_categories(self):
        return Category.query.all()

    def create_category(self, name):
        category = Category(name=name)
        self.db.session.add(category)
        self.db.session.commit()
        return category

    def get_category_by_id(self, category_id):
        return Category.query.get(category_id)

    def update_category(self, category_id, name):
        category = Category.query.get(category_id)

        if category:
            category.name = name
            self.db.session.commit()

        return category
