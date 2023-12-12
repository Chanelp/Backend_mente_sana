# server
from fastapi import HTTPException

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

    def get_all_therapists(self, limit):
        therapists = self.db.query(TherapistModel).limit(limit).all()
        return therapists