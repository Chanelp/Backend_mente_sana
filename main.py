from fastapi import FastAPI
from config.database import Base, engine, Session
from routers.user import user_router
from routers.therapist import therapist_router
import uvicorn
import os

from datetime import datetime 

app = FastAPI()
app.title = "API para la plataforma de salud mental en línea."

app.include_router(user_router)
app.include_router(therapist_router)

def init_db():
    from models import user, therapy_patients, therarpist, therapy_session, statuses
    Base.metadata.create_all(bind = engine)

    s = Session()
    newUser = user.UserModel()
    
    newUser.name = "pedro mir"
    newUser.last_name = "alberto gilberto"
    newUser.email = "emailNoGris@gmail.com"
    newUser.password = "sinHash"
    newUser.genre = "masculino"

    s.add(newUser)
    
    s.commit()
    print('database intialized :D')

if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
    
