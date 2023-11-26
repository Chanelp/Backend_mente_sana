from fastapi import FastAPI
from config.database import Base, engine
from routers.user import user_router
from routers.therapist import therapist_router
import uvicorn
import os

app = FastAPI()
app.title = "API para la plataforma de salud mental en línea."

app.include_router(user_router)
app.include_router(therapist_router)

Base.metadata.create_all(bind = engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))