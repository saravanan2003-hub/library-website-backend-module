from .user_validator import UserValidator
from .user_model import userDAO
from .user_schema import UserCreate
from uuid import UUID


class UserService:
    def create_user(self, user_data:UserCreate):
        user = userDAO.create_user(self, user_data)
        return user
    
    def get_all_user(self):
        users = userDAO.get_users(self)
        return users
    
    def get_user_by_id(self, user_id: str):
        UserValidator.validate_user_id(self, user_id)
        # user_id = UUID(id)
        user = userDAO.get_user_by_id(self, user_id)
        return user
    
    def update_user(self, user_id:UUID , user_data:UserCreate):
        UserValidator.validate_user_id(self, user_id)
        user = userDAO.update_user(self, user_id, user_data)
        return user
    
    def get_user_by_email(self, email:str):
        user = userDAO.get_user_by_email(self, email)
        return user
