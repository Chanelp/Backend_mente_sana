from models.therapy_session import TherapySessionModel 
from sqlalchemy.orm import Session 

class TherapySessionServices:
    def __init__(self, db:Session) -> None:
        self.db = db

    def getAllSessions(self) -> list:
        try:
            sesiones = self.db.query(TherapySessionModel).all()
        except Exception:
            raise

        else:
            return sesiones
        