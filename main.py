from fastapi import FastAPI
from config.database import Base, engine
import uvicorn
import os

# Routers import
from routers.user import user_router
from routers.therapist import therapist_router
from routers.therapy_session import therapy_router
from routers.auth import auth_router

import json

# jwt and env
from dotenv import load_dotenv
from jwt import decode



app = FastAPI()
app.title = "API para la plataforma de salud ental en línea."

# routers
app.include_router(user_router)
app.include_router(therapist_router)
app.include_router(therapy_router)
app.include_router(auth_router)

def init_db():
    from models import user, therarpist, therapy_session, statuses
    Base.metadata.create_all(bind = engine)

    # Create default data
    statuses.StatusesModel.create_default_records()

    print('database intialized :D')

if __name__ == "__main__":
    import os
    load_dotenv()
    init_db()

    print(os.getenv('encrypt_pass'))
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
    
