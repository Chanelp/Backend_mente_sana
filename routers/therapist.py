# SERVER
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Schemas
from schemas.therapist import Therapist

# Services
from services.therapist import TherapistService

# database
from config.database import Session
from typing import List

# MIDDLEWARES
from middlewares.auth import verify_JSON_web_token

# Utils
from utils.customException import CustomException

# ORM
from sqlalchemy.exc import SQLAlchemyError


therapist_router = APIRouter(prefix='/therapist')

    
@therapist_router.get(path="/therapists/}", tags=["Therapists"], status_code=200, response_model=List[Therapist])
def get_all_therapists(limit: int = 10):
    try:
        db = Session()
        all_therapists = TherapistService(db).get_all_therapists(limit)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))

    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=400)

    else:

        if not all_therapists:
            return JSONResponse(status_code=404, content={"message":"Terapeutas no encontrados"})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(all_therapists))
    


@therapist_router.get(path='/my-profile', tags=['Therapists'], status_code=200, response_model=dict)
async def get_therapist_profile(request: Request):
    payload = verify_JSON_web_token(request)

    try:
        db = Session()
        therapist_data = TherapistService(db).get_therapist_profile(int(payload['sub']))
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(therapist_data))

@therapist_router.put(path='/change-status', tags=['Therapists'], status_code=200, response_model=dict)
async def change_status(request: Request, status:int):
    payload = verify_JSON_web_token(request)
    

    try:
        if status not in [1, 3]:
            raise Exception('Estatus no válido')

        db = Session()
        TherapistService(db).change_status(int(payload['sub']) ,status)

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    except CustomException as e:
        return JSONResponse(content={"message": e.message}, status_code=e.status_code)
    
    else:
        statusMessage = 'En linea' if status == 1 else 'Desconectado'
        return JSONResponse(status_code=200, content={"message": f"Ahora estas {statusMessage}."})
    
@therapist_router.put(path='/update-description', tags=['Therapists'], status_code=200, response_model=dict)
async def update_description(request: Request, description: str):
    payload = verify_JSON_web_token(request)

    if (not description or len(description.strip()) < 30):
        raise HTTPException(status_code=400, detail='Descripcion muy corta')

    try:
        db = Session()
        TherapistService(db).update_description(int(payload['sub']), description)

    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))

    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    else:
        return JSONResponse(status_code=200, content={"message": "Description actualizada correctamente"})
    
@therapist_router.put(path='/change-passoword', tags=['Therapists'], response_model=dict, status_code=200)
async def change_password(request: Request, actual_password:str, new_password:str):
    payload = verify_JSON_web_token(request)

    try:
        db = Session()
        TherapistService(db).change_password(int(payload['sub']), actual_password, new_password)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    except CustomException as e:
        return JSONResponse(content={"message": e.message}, status_code=e.status_code)
    
    else:
        return JSONResponse(status_code=200, content={"message": "Contraseña cambiada correctamente"})