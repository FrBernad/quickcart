from abc import ABC, abstractmethod

class ShoppingCartDao(ABC):
    
    @abstractmethod
    def get_user_by_id(self,user_id):
        pass
        
    @abstractmethod
    def get_user_by_email(self,email):
        pass
    @abstractmethod
    def create_user(self,username, email, password):
        pass
    
    @abstractmethod
    def update_user(self,user, username, email):
        pass