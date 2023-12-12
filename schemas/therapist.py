from pydantic import BaseModel
from typing import Optional


class Therapist(BaseModel):
    id: Optional[int] = None
    name: str
    last_name: str
    email: str
    password: str
    professional_description: str
    specialty: str 
    license: str
    status_id: Optional[int] = 2

    model_config = {
        "json_schema_extra": {
        "examples": [{
                "name" : "Nombre del terapeuta",
                "last_name" : "apellido del terapeuta",

                "email" : "Email del terapeuta",
                "password" : "contraseña del terapeuta",

                "professional_description": "As a licensed psychologist, I am dedicated to providing compassionate and evidence-based therapy to individuals seeking support and personal growth.",
                "specialty": "children psicology",
                "license": "IDK",
            }]
        }
    }
