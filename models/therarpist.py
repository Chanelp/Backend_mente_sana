from config.database import Base, createAt
from sqlalchemy import Column, String, Integer, ForeignKey, CHAR

from models.statuses import StatusesModel

class TherapistModel(Base):
    
    __tablename__ = "therapist"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    professional_description = Column(String, nullable=True)
    specialty = Column(String, nullable=False)
    license = Column(String, nullable=False)

    status_id = Column(Integer, ForeignKey(StatusesModel.id))
    photo = Column(String, nullable=True)

    createAt = createAt.copy()