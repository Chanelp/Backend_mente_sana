from config.database import Base, createAt
# orm
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


from models.therarpist import TherapistModel
from models.user import UserModel
from models.statuses import StatusesModel

class TherapySessionModel(Base):
    
    __tablename__ = "therapy_session"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    therapist_name = Column(String, nullable=False)
    session_date = Column(String, nullable=False)
    session_time = Column(String, nullable=False)
    selected_service = Column(String, nullable=False)
    patient_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    price = Column(String, nullable=True)
    status_id = Column(Integer, ForeignKey(StatusesModel.id), nullable=False)
    
    createAt = createAt.copy()

    patient = relationship("UserModel", back_populates="therapies")