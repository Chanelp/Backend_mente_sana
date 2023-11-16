from fastapi import FastAPI
from config.database import Base, engine
from routers.user import user_router

app = FastAPI()
app.title = "API para la plataforma de salud mental en línea."

app.include_router(user_router)

Base.metadata.create_all(bind = engine)