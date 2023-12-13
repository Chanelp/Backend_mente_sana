from models.therarpist import TherapistModel
from models.user import UserModel
from sqlalchemy.orm import Session

# password hash
import bcrypt as hasher

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
        return therapists
    
    def get_therapist_profile(self, id:int) -> TherapistModel:
        therapist = self.db.query(TherapistModel).filter(TherapistModel.id == id).one_or_none()

        return therapist

    def change_status(self, therapistId: int, statusId:int):
        if statusId not in [1, 3]:
            raise Exception('Estatus no válido')
        
        therapist = self.db.get(TherapistModel, therapistId)
        
        therapist.status_id = statusId
        self.db.commit()

    def update_description(self, id:int, description:str):
        therapist = self.db.get(TherapistModel, id)

        therapist.professional_description = description

        self.db.commit()