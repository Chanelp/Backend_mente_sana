from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class therapy_session(BaseModel):
    id: Optional[int] = None
    therapist_id: int 
    session_date: datetime
    session_note: Optional[str] = None
    patient_id: int
    status_id:Optional[int] = 2

    createAt: Union[datetime, None] = datetime.now()
    
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "therapist_id": "Id del terapeuta de la session",
                "session_date": "fecha de inicio (full DateTime con la hora)",
                "session_note": "Nota de la sesion - (Description del usuario)",
                "patient_id": "Id del paciente"
            }]
        }
    }