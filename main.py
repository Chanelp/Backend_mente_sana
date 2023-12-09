<<<<<<< HEAD
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
=======
from fastapi import FastAPI
>>>>>>> e2711e5ecb229e7df69532523de5928cb9f21276
from config.database import Base, engine
import uvicorn
import os

# Routers import
from routers.user import user_router
from routers.therapist import therapist_router
from routers.therapy_session import therapy_router
from routers.auth import auth_router


app = FastAPI()
app.title = "API para la plataforma de salud ental en línea."

# Configuración de CORS para permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar los dominios permitidos en lugar de "*"
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar los métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Puedes especificar los encabezados permitidos
)

# routers
app.include_router(user_router)
app.include_router(therapist_router)
app.include_router(therapy_router)
app.include_router(auth_router)

# middlewares
from fastapi.middleware.cors import CORSMiddleware 
app.add_middleware(CORSMiddleware, 
    allow_origins=['*'], 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"])

def init_db():
    from models import user, therarpist, therapy_session, statuses
    Base.metadata.create_all(bind = engine)

    # Create default data
    statuses.StatusesModel.create_default_records()

    print('database intialized :D')

if __name__ == "__main__":
    import utils.env as env
    init_db()

#   Code to load .env files to envoirements variables 
    from dotenv import load_dotenv
    load_dotenv()

    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
    
