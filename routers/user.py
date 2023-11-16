from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import User
from services.user import UserService
from config.database import Session

user_router = APIRouter()

@user_router.post(path= "/users", tags= ["Users"], response_model= dict, status_code= 201)
async def create_user(new_user: User) -> dict:
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
    else:
        UserService(db).register_user(new_user)
        return JSONResponse(content= {"message": "Usuario registrado exitosamente!"}, status_code= 201)

