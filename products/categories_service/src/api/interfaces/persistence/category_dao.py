from abc import ABC, abstractmethod


class CategoryDao(ABC):
    @abstractmethod
    def create_category(self, name):
        pass

    @abstractmethod
    def get_categories(self):
        pass

    @abstractmethod
    def update_category(self, category, name):
        pass

    @abstractmethod
    def get_category_by_id(self, category_id):
        pass
