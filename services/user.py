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
    
    def delete_user(self, id: int):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()

    def get_all_users(self):
        users = self.db.query(UserModel).all()
        return users
    
    def get_user(self, id: int):
        user_searched = self.db.query(UserModel).filter(UserModel.id == id).first()
        return user_searched
    
    def update_user_info(self, id:int, new_data: User):
        user_searched: User = self.get_user(id)

        user_searched.name = new_data.name
        user_searched.last_name = new_data.last_name
        user_searched.email = new_data.email
        user_searched.password = new_data.password
        user_searched.genre = new_data.genre
        user_searched.date_birth = new_data.date_birth

        self.db.add(user_searched)
        self.db.commit()
        self.db.refresh(user_searched)