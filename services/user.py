from schemas.user import User
from models.user import UserModel

class UserService:
    def __init__(self, db):
        self.db = db
    
    def register_user(self, user):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()