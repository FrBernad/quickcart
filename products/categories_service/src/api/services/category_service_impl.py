from src.api.interfaces.services.category_service import CategoryService
from src.api.interfaces.persistence.category_dao import CategoryDao
from src.api.interfaces.exceptions.category_not_found_exception import (
    CategoryNotFoundException,
)
from injector import inject


class CategoryServiceImpl(CategoryService):
    @inject
    def __init__(self, category_dao: CategoryDao):
        self.category_dao = category_dao

    def create_category(self, name):
        return self.category_dao.create_category(name=name)

    def get_categories(self):
        return self.category_dao.get_categories()

    def get_category_by_id(self, category_id):
        category = self.category_dao.get_category_by_id(category_id=category_id)
        if not category:
            raise CategoryNotFoundException()
        return category

    def update_category(self, category_id, name):
        category = self.get_category_by_id(category_id=category_id)
        return self.category_dao.update_category(category, name=name)
