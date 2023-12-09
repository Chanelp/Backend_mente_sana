from config.database import Base, createAt
from sqlalchemy import Column, String, Integer, ForeignKey

from models.statuses import StatusesModel
from models.user import UserModel

class TherapistModel(Base):
    
    __tablename__ = "therapist"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    professional_description = Column(String)
    specialty = Column(String)
    license = Column(String)
    status_id = Column(Integer, ForeignKey(StatusesModel.id))
    user_id = Column(Integer, ForeignKey(UserModel.id))

    createAt = createAt.copy()