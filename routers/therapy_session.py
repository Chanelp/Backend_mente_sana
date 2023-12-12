from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.therapy_session import TherapySessionServices
from config.database import Session
from typing import List

therapy_router = APIRouter()


@therapy_router.post(path='/therapy_sessions/{id}', tags=['Therapy session'], response_model=dict, status_code=200)
def get_sesion_by_therapist(id:int) -> dict:
    try:
        service = TherapySessionServices(Session())
        sesiones = service.getSessionsByTherapist(id)
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

    else:
        return JSONResponse(content= jsonable_encoder(sesiones), status_code= 200)