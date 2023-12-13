# ORM
from sqlalchemy.orm import Session

# Schema
from schemas.injuries import injuries

# models
from models.injuries import InjuriesModel


class injuriesService:
    def __init__(self, db: Session) -> None:
        self.db = db
    
    def add_injurie(self, injury: injuries):

        new_injury = InjuriesModel(**injury.model_dump())


        self.db.add(new_injury)
        self.db.commit()