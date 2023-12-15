# Server
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Schemas
from schemas.user import User

# Services
from services.user import UserService

# Config / db
from config.database import Session
from typing import List

# ORM
from sqlalchemy.exc import SQLAlchemyError

# Utils
from utils.customException import CustomException

# middleware
from middlewares.auth import verify_JSON_web_token

user_router = APIRouter(prefix='/user')
    
@user_router.get(path="/users", tags=["Users"], status_code=200, response_model=List[User])
def get_all_users():
    try:
        db = Session()
        all_users = UserService(db).get_all_users()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))
    

    else:

        if not all_users:
            return JSONResponse(status_code=404, content={"message":"Usuarios no encontrados"})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(all_users))

@user_router.get(path="/user/{id}", tags=["Users"], response_model=User, status_code=200)
def get_one_user(id: int):
    try:
        db = Session()
        user_searched = UserService(db).get_user(id)

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

    else:

        if not user_searched:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado."})
        
        return JSONResponse(status_code=200, content=jsonable_encoder(user_searched))

@user_router.put(path="/user/{id}", tags=["Users"], response_model=dict, status_code=200)
def update_user(id: int, user: User):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))

    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

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
        user_delete = UserService(db).delete_user(id)

    except HTTPException as e:
        raise HTTPException(status_code= 500, detail=str(e))

    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))    

    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

    else:

        if user_delete < 1:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
        
        return JSONResponse(status_code=200, content={"message":"Usuario eliminado correctamente!"})
    
@user_router.put(path='/change_password', tags=['Users'], response_model=dict, status_code=200)
async def change_password(request: Request, new_password:str, actual_password:str):

    payload = verify_JSON_web_token(request)

    try:
        db = Session()
        UserService(db).change_password(int(payload['sub']), actual_password, new_password)
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail=str(e))

    except SQLAlchemyError as e:
        raise HTTPException(status_code = 400, detail = str(e))    
    
    except CustomException as e:
        raise HTTPException(e.status_code, e.message)
    else:
        
        return JSONResponse({"message": "Contraseña cambiada correctamente"}, 200)