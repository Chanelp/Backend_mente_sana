from schemas.user import User
from models.user import UserModel


class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, user):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()

    def login_user(self, email:str, password:str):
        user_searched = self.db.query(UserModel).filter(UserModel.email == email).one_or_none()
        return user_searched