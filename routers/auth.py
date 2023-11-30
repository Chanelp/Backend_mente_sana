from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User
from services.user import UserService
from config.database import Session
from typing import List


auth_router = APIRouter()

@auth_router.post(path= "/users", tags= ["Auth"], response_model= dict, status_code= 201)
async def create_user(new_user: User) -> dict:
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
    else:
        added_user = UserService(db).register_user(new_user)
        return JSONResponse(content= {"message": "Usuario registrado exitosamente!"}, status_code= 201)

@auth_router.get(path="/login", tags = ["Auth"], response_model=dict, status_code= 200)
def login(email:str, password:str):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail= str(e))
    
    else:
        response = UserService(db).login_user(email, password)

        print(response['invalid'])
        
        if bool(response["invalid"]):
            return JSONResponse(status_code=404, content={"message":"Usuario o contraseña incorrecta"})

        return JSONResponse(status_code=200, content={"message":"Inicio de sesión exitoso"})