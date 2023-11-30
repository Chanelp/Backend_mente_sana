from config.database import Base, createAt
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float

from models.therarpist import TherapistModel
from models.user import UserModel
from models.statuses import StatusesModel

class TherapySessionModel(Base):
    
    __tablename__ = "therapy_session"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    therapist_id = Column(Integer, ForeignKey(TherapistModel.id), nullable=False)
    start_date = Column(Date, nullable=False)
    session_duration = Column(int, nullable=True, default=None) ## Minutos (Mins)
    session_note = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    status_id = Column(Integer, ForeignKey(StatusesModel.id), nullable=False)
    
    createAt = createAt.copy()
