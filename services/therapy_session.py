from models.therapy_session import TherapySessionModel 
from sqlalchemy.orm import Session 

class TherapySessionServices:
    def __init__(self, db:Session) -> None:
        self.db = db

    def getSessionsByTherapist(self, id:int) -> list:
        try:
            sesiones = self.db.query(TherapySessionModel).filter(TherapySessionModel.id == id)
        except Exception:
            raise

        else:
            return sesiones
        