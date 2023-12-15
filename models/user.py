from config.database import Base, createAt


# ORM
from sqlalchemy import Column, String, Integer, DateTime, CHAR, ForeignKey
from sqlalchemy.orm import relationship

# Models
from models.therarpist import TherapistModel

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(CHAR(60) , nullable=False)
    genre = Column(String)
    date_birth = Column(DateTime, nullable=False)

    rol = Column(String, default='user')
    
    createAt = createAt.copy()

    therapies = relationship("TherapySessionModel", back_populates="patient")

