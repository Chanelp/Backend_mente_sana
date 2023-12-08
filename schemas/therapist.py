from pydantic import BaseModel
from typing import Optional


class Therapist(BaseModel):
    id: Optional[int] = None
    user_id: int
    professional_description: str
    specialty: str 
    license: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "user_id": 1, # user_id -> FK, need to exists to create a new therapist
                "professional_description": "As a licensed psychologist, I am dedicated to providing compassionate and evidence-based therapy to individuals seeking support and personal growth.",
                "specialty": "children psicology",
                "license": "IDK"
            }]
        }
    }
