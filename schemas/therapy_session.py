from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class therapy_session(BaseModel):
    id: Optional[int] = None
    therapist_name: str 
    session_date: str
    session_time: str
    selected_service: str
    patient_id: int
    price: Optional[str] = None 
    status_id:Optional[int] = 1

    createAt: Union[datetime, None] = datetime.now()
    
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "therapist_name": "nombre del terapeuta de la session",
                "session_date": "fecha de inicio (string)",
                "session_time": "hora de la sesion",
                "selected_service": "Servicio seleccionado",
                "patient_id": "Id del paciente",
                "price": "precio de la sesion"
            }]
        }
    }