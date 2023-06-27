from src.api.interfaces.services.user_service import UserService
from src.api.interfaces.persistence.user_dao import UserDao
from injector import inject

class UserServiceImpl(UserService):

    @inject
    def __init__(self, userDao: UserDao):
        self.userDao = userDao
    
    def get_user_by_email(self, email):
        return self.userDao.get_user_by_email(email)
    
    def get_user_by_id(self, id):
        return self.userDao.get_user_by_id(id)
    
    def create_user(self, username, email,password):
        return self.userDao.create_user(username, email,password)
     
    def update_user(self, user,username,password):
        return self.userDao.update_user(user, username,password)
    
   
    

    


   
    

    

