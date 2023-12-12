from models.therarpist import TherapistModel
from models.user import UserModel
from sqlalchemy.orm import Session

class TherapistService:
    def __init__(self, db:Session):
        self.db = db
    
    def register_therapist(self, therapist, user_id: int):
        user = self.db.get(UserModel, user_id) 

        if (user.therapist_id != None):
            raise Exception('Este usuario ya es terapeuta')


        new_therapist = TherapistModel(**therapist.model_dump())
        self.db.add(new_therapist)
        

        self.db.flush()

        user.therapist_id = new_therapist.id

        self.db.commit()
        return new_therapist

    def get_all_therapists(self, limit):
        therapists = self.db.query(TherapistModel).limit(limit).all()
        return therapists