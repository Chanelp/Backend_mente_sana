from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from schemas.user import User
from services.user import UserService
from config.database import Session
import jwt
from utils.env import read_env_key 
SECRET = read_env_key('encrypt_pass')



auth_router = APIRouter(prefix='/auth')

@auth_router.post(path= "/register", tags= ["Auth"], response_model= dict, status_code= 201)
async def create_user(new_user: User) -> dict:
    payload = {"sub": ""}
    try:
        db = Session()
        added_user = UserService(db).register_user(new_user)

    except HTTPException as e:
        raise HTTPException(status_code = 500, detail = str(e))

    else:
        payload["sub"] = added_user.id
        token = jwt.encode(payload, SECRET, algorithm='HS256')
        return JSONResponse(content= {"message": "Usuario registrado exitosamente!", "jwToken": token}, status_code= 201)

@auth_router.post(path="/login", tags = ["Auth"], response_model=dict, status_code= 200)
def login(email:str, password:str, request: Request):
    try:
        db = Session()
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail= str(e))
    
    else:
        response = UserService(db).login_user(email, password)

        if bool(response["invalid"]):
            return JSONResponse(status_code=404, content={"message":"Usuario o contraseña incorrecta"})
        
        payload = {"sub": ""}

        payload["sub"] = response['id']
        tkn = jwt.encode(payload, SECRET, algorithm='HS256')

        return JSONResponse(status_code=200, content={"message":"Inicio de sesión exitoso", "token": tkn})