from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from models import *
from typing import Annotated
from sqlmodel import Session, select
from dependencies import get_session, KEY
from autentication import user_of_token

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/categoria/registrar", status_code=201)
def create_category(category: Category, session: SessionDep, Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    user = user_of_token(session, KEY, Authorization)
    if user:
        existent_category = session.scalar(select(Category).where(Category.name == category.name))

        if not existent_category:
            new_category = Category (
                name = category.name,
                details = category.details,
                user = user
            )
            session.add(new_category) # cria nova categoria
            session.commit()
            session.refresh(new_category)
        else:
            raise HTTPException(status_code=409, detail=f"Categoria já cadastrada")

@router.get("/categorias", status_code=200)
def categorias(session: SessionDep, Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    user = user_of_token(session, KEY, Authorization)
    if user:
        return session.exec(select(Category).where(Category.user == user)).all()