from config.database import Base, createdDate
from sqlalchemy import Column, String, Integer, DateTime, CHAR

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(CHAR(60) , nullable=False)
    genre = Column(String)
    date_birth = Column(DateTime, nullable=False)
    rol = Column(String)
    
    createdDate = createdDate._clone()


