from fastapi import FastAPI
from database import lifespan
from endpoints import user

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)