# Server
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Services
from services.therapy_session import TherapySessionServices

# Config
from config.database import Session
from typing import List

# Schemas
from schemas.therapy_session import therapy_session

# middlewares
from middlewares.auth import verify_JSON_web_token

from utils.customException import CustomException

therapy_router = APIRouter(prefix='/therapy')

TAGS = ['Therapy session']


@therapy_router.get(path='/therapy_sessions/{id}', tags=TAGS, response_model=dict, status_code=200)
async def get_sesion_by_therapist() -> dict:
    try:
        db = Session()
        sesiones = TherapySessionServices(db).getSessionsByTherapist()
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

    else:
        db.close()
        return JSONResponse(content= jsonable_encoder(sesiones), status_code= 200)
    
@therapy_router.post(path='/new-therapy', tags=TAGS, response_model=List[dict], status_code=200)
async def create_therapy(therapy: therapy_session) -> dict:    

    try:
        db = Session()
        TherapySessionServices(db).createTherapy(therapy)
    except HTTPException as e:
        raise HTTPException(400, str(e))
    
    except CustomException as e:
        raise HTTPException(e.status_code, e.message)
    
    else:
        db.close()
        return JSONResponse({"message":"Solicitud de terapia enviada correctamente"}, 200)
    
@therapy_router.put('/accept_session/{therapyId}', status_code=200, response_model=dict, tags=TAGS)
async def accept_therapy(request: Request, therapyId:int):
    payload = verify_JSON_web_token(request, 'therapist')

    try:
        db = Session()
        TherapySessionServices(db).accept_therapy(therapyId, int(payload['sub']))
    except HTTPException as e:
        raise HTTPException(400, str(e))
    
    except CustomException as e:
        raise HTTPException(e.status_code, e.message)
    
    else:
        db.close()
        return JSONResponse({"message":"Solicitud aceptada correctamente"}, 200)
    
@therapy_router.put('/reject_session/{therapyId}', status_code=200, response_model=dict, tags=TAGS)
async def reject_therapy(request: Request, therapyId:int):
    payload = verify_JSON_web_token(request, 'therapist')

    try:
        db = Session()
        TherapySessionServices(db).reject_therapy(therapyId, int(payload['sub']))
    except HTTPException as e:
        raise HTTPException(400, str(e))
    
    except CustomException as e:
        raise HTTPException(e.status_code, e.message)
    
    else:
        db.close()
        return JSONResponse({"message":"Solicitud aceptada correctamente"}, 200)