# ORM
from sqlalchemy.orm import Session

# Schemas
from schemas.user import User

# Models
from models.user import UserModel
from models.therapy_session import TherapySessionModel

# Encrypting
import bcrypt

# Utils
from utils.customException import CustomException

class UserService:
    def __init__(self, db:Session):
        self.db = db

    def register_user(self, user):
        new_user = UserModel(**user.model_dump())

        # generate salt
        salt = bcrypt.gensalt()
        new_user.password = bcrypt.hashpw(new_user.password.encode(), salt).decode()
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def login_user(self, email:str, password:str) -> UserModel:
        user_searched = self.db.query(UserModel).filter(UserModel.email == email).one_or_none()
        
        if (not user_searched or not bcrypt.checkpw(password.encode(), user_searched.password.encode())):
            raise CustomException('Usuario o contraseña incorrecta', 401)
        
        return user_searched
    
    def delete_user(self, id: int):
        deleted = self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()

        return deleted

    def get_all_users(self):
        users = self.db.query(UserModel).all()
        return users
    
    def get_user(self, id: int):
        user_searched = self.db.get(UserModel, id)
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

    def get_user_sessions(self, id:int):
        user_sessions = self.db.query(TherapySessionModel).filter(TherapySessionModel.patient_id == id).all()

        return user_sessions

    def change_password(self, id:int, actual_password:str, new_password:str):
        user = self.db.get(UserModel, id)
        pass

        
