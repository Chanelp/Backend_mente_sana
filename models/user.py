from config.database import Base, createdDate
from sqlalchemy import Column, String, Integer, DateTime

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    genre = Column(String)
    date_birth = Column(DateTime)
    rol = Column(String)
    
    createdDate = createdDate._clone()


