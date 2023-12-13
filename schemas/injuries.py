# baseModel
from pydantic import BaseModel

# typing
from typing import Optional


class injuries(BaseModel):

    id: Optional[int] = None
    name:str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "Nombre de la enfermedad",
            }]
        }
    }