from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User
from services.user import UserService
from config.database import Session
from typing import List

from middlewares.auth import verify_JSON_web_token


user_router = APIRouter(prefix='/user')
    
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

@user_router.get(path="/user/{id}", tags=["Users"], response_model=User, status_code=200)
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

@user_router.put(path="/user/{id}", tags=["Users"], response_model=dict, status_code=200)
def update_user(id: int, user: User):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    else:
        user_to_update = UserService(db).get_user(id)

        if not user_to_update:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado."})
        
        UserService(db).update_user_info(id, user)
        return JSONResponse(status_code=200, content={"message":"Datos del usuario actualizados correctamente."})

@user_router.delete(path="/user/{id}", tags=["Users"], response_model=dict, status_code=200)
def delete_user(id: int):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail=str(e))
    
    else:
        user_delete = UserService(db).delete_user(id)

        if user_delete < 1:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
        
        return JSONResponse(status_code=200, content={"message":"Usuario eliminado correctamente!"})