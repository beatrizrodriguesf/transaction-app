from sqlalchemy import create_engine
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)
KEY = getenv("SECRET_KEY", "trans@ctIOnAPP")

# Cria banco de dados se não existir e conecta
engine = create_engine(f"sqlite:///database.db")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # código a ser executado antes de iniciar o servidor
    SQLModel.metadata.create_all(engine)
    yield
    # código a ser executado após o servidor ser encerrado

def get_session():
    with Session(engine) as session:
        yield session