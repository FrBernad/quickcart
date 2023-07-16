from src.api.interfaces.services.tag_service import TagService
from src.api.interfaces.persistence.tag_dao import TagDao
from injector import inject


class TagServiceImpl(TagService):

    @inject
    def __init__(self, tag_dao: TagDao):
        self.tag_dao = tag_dao

    def get_user_by_email(self, email):
        return self.tag_dao.get_user_by_email(email=email)

    def get_user_by_id(self, user_id):
        return self.tag_dao.get_user_by_id(user_id=user_id)

    def create_user(self, username, email, password):
        return self.tag_dao.create_user(username=username, email=email, password=password)

    def update_user(self, user, username, password):
        return self.tag_dao.update_user(user=user, username=username, password=password)
