from config.database import Base, createAt
from sqlalchemy import Column, String, Integer, ForeignKey

from models.statuses import StatusesModel

class TherapistModel(Base):
    
    __tablename__ = "therapist"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    professional_description = Column(String)
    specialty = Column(String)
    license = Column(String)
    status_id = Column(Integer, ForeignKey(StatusesModel.id))

    createAt = createAt.copy()