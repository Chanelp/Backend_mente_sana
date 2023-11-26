from config.database import Base
from sqlalchemy import Column, String, Integer

class TherapistModel(Base):
    
    __tablename__ = "therapist"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    professional_description = Column(String)
    specialty = Column(String)
    license = Column(String)
