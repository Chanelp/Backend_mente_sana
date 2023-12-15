# ORM
from sqlalchemy.orm import Session

# Schema
from schemas.injuries import injuries

# models
from models.injuries import InjuriesModel

# utils
from typing import List
from utils.customException import CustomException


class injuriesService:
    def __init__(self, db: Session) -> None:
        self.db = db
    
    def add_injurie(self, injury: injuries):

        new_injury = InjuriesModel(**injury.model_dump())


        self.db.add(new_injury)
        self.db.commit()
        self.db.close()

    def get_injuries(self, page:int, limit:int) -> List[InjuriesModel]:
        injuries = self.db.query(InjuriesModel).limit(limit).offset(page*limit).all()

        if len(injuries) == 0:
            raise CustomException('No hay más enfermedades', 404)
        
        self.db.close()
        return injuries
