from models.therarpist import TherapistModel
from models.user import UserModel
from sqlalchemy.orm import Session

# password hash
import bcrypt as hasher

#utils 
from utils.customException import CustomException

# services
from services.therapy_session import TherapySessionServices

class TherapistService:
    def __init__(self, db:Session):
        self.db = db
    
    def register_therapist(self, therapist):
        new_therapist = TherapistModel(**therapist.model_dump())

        new_salt = hasher.gensalt()
        new_therapist.password = hasher.hashpw(new_therapist.password.encode(), new_salt).decode()
        
        self.db.add(new_therapist)
        self.db.flush()
        self.db.commit()
        return new_therapist

    def login_therapist(self, email:str, password:str):
        therapist = self.db.query(TherapistModel).filter(TherapistModel.email == email).one_or_none()
        
        invalidLogin = not therapist or not hasher.checkpw(password.encode(), therapist.password.encode())
        
        return {"invalid": invalidLogin, "userData": therapist}

    def get_all_therapists(self, limit):
        therapists = self.db.query(TherapistModel).limit(limit).all()
        self.db.close()
        return therapists
    
    def get_therapist_profile(self, id:int) -> TherapistModel:
        therapist = self.db.query(TherapistModel).filter(TherapistModel.id == id).one_or_none()

        sessionsService = TherapySessionServices(self.db)

        sessions = sessionsService.getSessionsByTherapist(id)

        pending_sessions = sessionsService.getPendingSessions(id)

        self.db.close()
        return {**therapist.__dict__, "sessions": sessions, "pending_sessions": pending_sessions}

    def change_status(self, therapistId: int, statusId:int):
    
        therapist = self.db.get(TherapistModel, therapistId)

        if statusId == therapist.status_id:
            raise CustomException('Ya estás en ese estado. Sin modificaciones.', 400)
        
        therapist.status_id = statusId
        self.db.commit()

    def update_description(self, id:int, description:str):
        therapist = self.db.get(TherapistModel, id)

        therapist.professional_description = description

        self.db.commit()
        self.db.close()

    def change_password(self, id:int, actual_password:str, new_password:str):
        
        therapist_account = self.db.get(TherapistModel, id)

        if (not self.verify_old_password(actual_password, therapist_account.password)): raise CustomException('Contraseña actual invalida', 400)
        
        therapist_account.password = hasher.hashpw(new_password.encode(), hasher.gensalt())
        self.db.commit()
        self.db.close()


    def verify_old_password(self, password:str, hashed_password:str) -> bool:
        return hasher.checkpw(password.encode(), hashed_password.encode())
    
    def get_active_therapists(self):
        active_therapists = self.db.query(TherapistModel).filter(TherapistModel.status_id == 1).all()
        self.db.close()

        return active_therapists
