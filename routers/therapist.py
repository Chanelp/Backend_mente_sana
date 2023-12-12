# SERVER
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.therapist import Therapist

from services.therapist import TherapistService

from config.database import Session
from typing import List

# ENVOIREMENT
from utils.env import read_env_key

# JSON WEB TOKEN
import jwt

# MIDDLEWARES
from middlewares.auth import verify_JSON_web_token

therapist_router = APIRouter()
SECRET = read_env_key("encrypt_pass")

@therapist_router.post(path= "/new-therapist", tags= ["Therapists"], response_model= dict, status_code= 201)
async def create_therapist(new_therapist: Therapist, request: Request) -> dict:
    validatedPayload = verify_JSON_web_token(request)
    try:
        db = Session()

        added_therapist = TherapistService(db).register_therapist(new_therapist, int(validatedPayload['sub']))

        validatedPayload['therapist_id'] = added_therapist.id
        
        new_token = jwt.encode(validatedPayload, SECRET, "HS256")
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))
    else:
        
        return JSONResponse(content= {"message": "Terepeuta registrado exitosamente!", "new_token": new_token}, status_code= 201)
    
@therapist_router.get(path="/therapists/}", tags=["Therapists"], status_code=200, response_model=List[Therapist])
def get_all_therapists(limit: int = 10):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

    else:
        all_therapists = TherapistService(db).get_all_therapists(limit)

        if not all_therapists:
            return JSONResponse(status_code=404, content={"message":"Terapeutas no encontrados"})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(all_therapists))