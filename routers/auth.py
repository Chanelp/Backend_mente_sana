# Server
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

# Schemas
from schemas.user import User
from schemas.therapist import Therapist

# Services
from services.user import UserService
from services.therapist import TherapistService

# Config
from config.database import Session

# JSON web token
import jwt

# ORM
from sqlalchemy.exc import SQLAlchemyError 

# Utils
from utils.env import read_env_key 
from utils.customException import CustomException


# Encoding secret to JWT
SECRET = read_env_key('encrypt_pass')

TAGS = ['Auth']

auth_router = APIRouter(prefix='/auth')

@auth_router.post(path= "/register", tags= TAGS, response_model= dict, status_code= 201)
async def create_user(new_user: User) -> dict:
    payload = {"sub": "", 'type': 'user'}
    try:
        db = Session()
        added_user = UserService(db).register_user(new_user)
        payload["sub"] = added_user.id
        print(SECRET)
        token = jwt.encode(payload, SECRET, algorithm='HS256')

    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))

    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail= str(e))

    else:
        db.close()
        return JSONResponse(content= {"message": "Usuario registrado exitosamente!", "jwToken": token}, status_code= 201)

@auth_router.post(path="/login", tags = TAGS, response_model=dict, status_code= 200)
def login(email:str, password:str, request: Request):
    try:
        db = Session()
        payload = {"sub": "", 'type': 'user'}

        response = UserService(db).login_user(email, password)

        payload["sub"] = response.id

        tkn = jwt.encode(payload, SECRET, algorithm='HS256')
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail= str(e))

    except CustomException as e:
        raise HTTPException(status_code = e.status_code, detail= e.message)

    else:
        db.close()
        return JSONResponse(status_code=200, content={"message":"Inicio de sesión exitoso", "token": tkn})
        

@auth_router.post(path= "/register-therapist", tags=TAGS, response_model= dict, status_code= 201)
async def create_therapist(new_therapist: Therapist) -> dict:
    try:
        db = Session()

        added_therapist = TherapistService(db).register_therapist(new_therapist)
        
        payload = {'sub': added_therapist.id, 'type': 'therapist'}
        token = jwt.encode(payload, SECRET, 'HS256')
        
    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    else:
        db.close()

        return JSONResponse(content= {"message": "Terepeuta registrado exitosamente!", "token": token}, status_code= 201)


@auth_router.post(path='/login-therapist', tags=TAGS, response_model=dict, status_code=201)
async def login_therapist(email:str, password:str):

    try:
        db = Session()
        response = TherapistService(db).login_therapist(email=email, password=password)
        payload = {"sub": "", 'type': 'therapist'}

        if bool(response["invalid"]):
            return JSONResponse(status_code=404, content={"message":"Usuario o contraseña incorrecta"})

        payload["sub"] = response['userData'].id

        tkn = jwt.encode(payload, SECRET, algorithm='HS256')
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    else:
        db.close()
        return JSONResponse(status_code=201, content={"message": "Therapeuta logueado correctamente", "token": tkn})