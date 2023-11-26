from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.therapist import Therapist
from services.therapist import TherapistService
from config.database import Session
from typing import List

therapist_router = APIRouter()

@therapist_router.post(path= "/therapists", tags= ["Auth"], response_model= dict, status_code= 201)
async def create_therapist(new_therapist: Therapist) -> dict:
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
    else:
        TherapistService(db).register_therapist(new_therapist)
        return JSONResponse(content= {"message": "Terepeuta registrado exitosamente!"}, status_code= 201)
    
@therapist_router.get(path="/therapists", tags=["Therapists"], status_code=200, response_model=List[Therapist])
def get_all_therapists():
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    else:
        all_therapists = TherapistService(db).get_all_therapists()

        if not all_therapists:
            return JSONResponse(status_code=404, content={"message":"Terapeutas no encontrados"})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(all_therapists))