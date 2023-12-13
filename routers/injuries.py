# fastapi
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# models
from models.injuries import InjuriesModel

# services
from services.injuries import injuriesService

# schemas
from schemas.injuries import injuries

# Config 
from config.database import Session
from typing import List

# utils
from utils.customException import CustomException

# ORM
from sqlalchemy.exc import SQLAlchemyError


injuries_router = APIRouter(prefix='/injuries')

@injuries_router.post(path='/new-injury', tags=['injuries'], response_model=dict, status_code=201)
async def add_injurie(request: Request, injury:injuries):
    try:
        db = Session()
        injuriesService(db).add_injurie(injury)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    else:
        return JSONResponse(status_code=201, content={"message": "Nueva etiqueta/enfermedad agregada correctamente"})
    
@injuries_router.get(path='/get-injuries', tags=['injuries'], response_model=List[injuries], status_code=201)
async def get_injuries(page:int, limit:int):
    try:
        db = Session()
        injuries = injuriesService(db).get_injuries(page, limit)
    except HTTPException as e:
        raise HTTPException(500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(500, str(e))
    
    except CustomException as e:
        raise HTTPException(e.status_code, e.message)
    
    else:
        return JSONResponse(content=jsonable_encoder(injuries), status_code=200)