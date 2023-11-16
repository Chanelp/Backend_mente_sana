from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str
    date_register: datetime | None = datetime.now()
    genre: str
    date_birth: date
    rol: str = "User"

    model_config = {
        "json_schema_extra":{
            "examples": [{
                    "name": "Nombre del usuario",
                    "email": "Correo electrónico",
                    "password": "Contraseña",
                    "date_birth": "Fecha nacimiento 0000-00-00",
                    "genre": "Género"
            }]
        }
    }
