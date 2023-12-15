from models.therapy_session import TherapySessionModel 
from sqlalchemy.orm import Session

# Schemas
from schemas.therapy_session import therapy_session

# models
from models.user import UserModel

# utils
from utils.customException import CustomException

from datetime import datetime

class TherapySessionServices:
    def __init__(self, db:Session) -> None:
        self.db = db

    def getSessionsByTherapist(self, id:int) -> list:
        sessions = self.db.query(TherapySessionModel).join(UserModel, UserModel.id == TherapySessionModel.patient_id).filter(
            TherapySessionModel.therapist_id == id, 
            TherapySessionModel.session_date > datetime.now(), 
            TherapySessionModel.status_id == 1).all()
        for sess in sessions:
            sess.patient

        return sessions
    

    def getPendingSessions(self, id: int):
        pending_sessions = self.db.query(TherapySessionModel).join(UserModel, UserModel.id == TherapySessionModel.patient_id).filter(
            TherapySessionModel.status_id == 2,
            TherapySessionModel.therapist_id == id,
            TherapySessionModel.session_date > datetime.now()).all()
        for sess in pending_sessions:
            sess.patient
        return pending_sessions
        
    

    def createTherapy(self, therapy:therapy_session):
        new_therapy = TherapySessionModel(**therapy.model_dump())
        self.db.add(new_therapy)
        self.db.commit()

    def accept_therapy(self, id:int, therapistId:int):
        therapy = self.db.get(TherapySessionModel, id)
        if therapistId != therapy.therapist_id:
            raise CustomException('Acción no válida', 401)

        therapy.status_id = 1
        self.db.commit()

    def reject_therapy(self, id:int, therapistId:int):
        therapy = self.db.get(TherapySessionModel, id)
        if therapistId != therapy.therapist_id:
            raise CustomException('Acción no válida', 401)

        therapy.status_id = 4
        self.db.commit()