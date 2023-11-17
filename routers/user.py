from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import User
from services.user import UserService
from config.database import Session

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