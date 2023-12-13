# fastapi
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

# models
from models.injuries import InjuriesModel

# services
from services.injuries import injuriesService

# schemas
from schemas.injuries import injuries

# Config 
from config.database import Session

injuries_router = APIRouter(prefix='/injuries')

@injuries_router.post(path='/new-injury', tags=['injuries'], response_model=dict, status_code=201)
async def add_injurie(request: Request, injury:injuries):
    try:
        db = Session()
        injuriesService(db).add_injurie(injury)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    else:
        return JSONResponse(status_code=201, content={"message": "Nueva etiqueta/enfermedad agregada correctamente"})