from pydantic import BaseModel
from typing import Optional


class Therapist(BaseModel):
    id: Optional[int] = None
    professional_description: str
    specialty: str 
    license: str
    status_id: Optional[int] = 2

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "professional_description": "As a licensed psychologist, I am dedicated to providing compassionate and evidence-based therapy to individuals seeking support and personal growth.",
                "specialty": "children psicology",
                "license": "IDK",
            }]
        }
    }
