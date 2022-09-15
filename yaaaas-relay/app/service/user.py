
from app.schema.user import UserCreate, UserUpdate


class UserService():
    def create_user(self, create_payload: UserCreate):
        raise NotImplementedError()
        
    def update_user(self, update_payload: UserUpdate):
        raise NotImplementedError()
    
    
user_service = UserService()