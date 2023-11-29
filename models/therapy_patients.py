from config.database import Base, createAt
from sqlalchemy import Column, String, Integer, ForeignKey
from models.user import UserModel
from models.therapy_session import TherapySessionModel


class TherapyPatients(Base):
    
    __tablename__ = "therapy_patients"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    session_id = Column(Integer, ForeignKey(TherapySessionModel.id))

    createdAt = createAt.copy()