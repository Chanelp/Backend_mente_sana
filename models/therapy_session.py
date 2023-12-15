from config.database import Base, createAt
# orm
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


from models.therarpist import TherapistModel
from models.user import UserModel
from models.statuses import StatusesModel

class TherapySessionModel(Base):
    
    __tablename__ = "therapy_session"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    therapist_id = Column(Integer, ForeignKey(TherapistModel.id), nullable=False)
    session_date = Column(DateTime, nullable=False)
    session_note = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    status_id = Column(Integer, ForeignKey(StatusesModel.id), nullable=False)
    
    createAt = createAt.copy()

    patient = relationship("UserModel", back_populates="therapies")