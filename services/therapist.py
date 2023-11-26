from models.therarpist import TherapistModel
from schemas.therapist import Therapist

class TherapistService:
    def __init__(self, db):
        self.db = db
    
    def register_therapist(self, therapist):
        new_therapist = TherapistModel(**therapist.model_dump())
        self.db.add(new_therapist)
        self.db.commit()

    def get_all_therapists(self):
        therapists = self.db.query(TherapistModel).alll()
        return therapists