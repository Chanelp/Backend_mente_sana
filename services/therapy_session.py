from models.therapy_session import TherapySessionModel 
from sqlalchemy.orm import Session 

# Schemas
from schemas.therapy_session import therapy_session

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
        
    def createTherapy(self, therapy:therapy_session):
        new_therapy = TherapySessionModel(**therapy.model_dump())
        self.db.add(new_therapy)
