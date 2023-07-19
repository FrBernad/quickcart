from src.api.interfaces.services.category_service import CategoryService
from src.api.interfaces.persistence.category_dao import CategoryDao
from injector import inject


class CategoryServiceImpl(CategoryService):

    @inject
    def __init__(self, category_dao: CategoryDao):
        self.category_dao = category_dao

    def create_category(self, name):
        return self.category_dao.create_category(name=name)

    def get_categories(self):
        return self.category_dao.get_categories()

    def update_category(self, category_id, name):
        return self.category_dao.update_category(category_id=category_id, name=name)
