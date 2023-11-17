from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User
from services.user import UserService
from config.database import Session
from typing import List

user_router = APIRouter()

@user_router.post(path= "/users", tags= ["Auth"], response_model= dict, status_code= 201)
async def create_user(new_user: User) -> dict:
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
    else:
        UserService(db).register_user(new_user)
        return JSONResponse(content= {"message": "Usuario registrado exitosamente!"}, status_code= 201)


@user_router.get(path="/login", tags = ["Auth"], response_model=dict, status_code= 200)
def login(email:str, password:str):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail= str(e))
    
    else:
        user_login = UserService(db).login_user(email, password)

        if not user_login or user_login.password != password:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
        
        return JSONResponse(status_code=200, content={"message":"Inicio de sesión exitoso"})
    

@user_router.get(path="/users", tags=["Users"], status_code=200, response_model=List[User])
def get_all_users():
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    else:
        all_users = UserService(db).get_all_users()

        if not all_users:
            return JSONResponse(status_code=404, content={"message":"Usuarios no encontrados"})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(all_users))

@user_router.get(path="/users/{id}", tags=["Users"], response_model=User, status_code=200)
def get_one_user(id: int):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    else:
        user_searched = UserService(db).get_user(id)

        if not user_searched:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado."})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(user_searched))

@user_router.delete(path="/login/{id}", tags=["Users"], response_model=dict, status_code=200)
def delete_user(id: int):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail=str(e))
    
    else:
        user_delete = UserService(db).delete_user(id)

        if not user_delete:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
        
        return JSONResponse(status_code=200, content={"message":"Usuario eliminado correctamente!"})