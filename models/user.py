from config.database import Base, createAt

from sqlalchemy import Column, String, Integer, DateTime, CHAR, ForeignKey

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

    therapist_id = Column(Integer, ForeignKey(TherapistModel.id), nullable=True)

    rol = Column(String, default='user')
    
    createAt = createAt.copy()

