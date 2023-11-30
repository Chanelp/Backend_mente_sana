from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class therapy_model(BaseModel):
    id: Optional[int] = None
    therapist_id: int 
    start_date: datetime
    session_duration: int # Duracion en minutos 
    session_note: str
    patient_id: int
    status_id:int

    createAt: Union[datetime, None] = datetime.now()
    
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "therapist_id": "Id del terapeuta de la session",
                "start_date": "fecha de inicio (Con hora)",
                "session_duration": "Duracion de la sesion (En minutos)",
                "patient_id": "Id del paciente",
                "status_id": "id del status de la sesion"
            }]
        }
    }