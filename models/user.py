from config.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
from datetime import datetime

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    date_register = Column(DateTime, default= datetime.utcnow)
    genre = Column(String)
    date_birth = Column(Date)
    rol = Column(String)
