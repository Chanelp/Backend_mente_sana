from config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float

from models.therarpist import TherapistModel

class TherapySessionModel(Base):
    
    __tablename__ = "therapy_session"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    therapist_id = Column(Integer, ForeignKey(TherapistModel.id), nullable=False)
    start_date = Column(Date, nullable=False)
    session_duration = Column(Float, nullable=False) ## Minutos (Mins)
    session_note = Column(String, nullable=False)
    
