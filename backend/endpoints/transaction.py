from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from models import *
from typing import Annotated
from sqlmodel import Session, select
from dependencies import get_session, KEY
from autentication import user_of_token

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/transacao/registrar", status_code=201)
def create_transaction(transaction: TransactionCreate, session: SessionDep, Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    user = user_of_token(session, KEY, Authorization)
    print(user)
    if user:
        existent_category = session.scalar(select(Category).where(Category.user == user, Category.name == transaction.category))
        if existent_category:
            new_transaction = Transaction(
                type = transaction.type,
                date = transaction.date,
                value = transaction.value,
                details = transaction.details,
                category = transaction.category,
                user = user
            )
            session.add(new_transaction) # cria nova transação
            session.commit()
            session.refresh(new_transaction)
        else:
            raise HTTPException(status_code=409, detail=f"Categoria não existente")

@router.get("/transacoes", status_code=200)
def transactions(session: SessionDep, Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    user = user_of_token(session, KEY, Authorization)
    if user:
        return session.exec(select(Transaction).where(Transaction.user == user)).all()

@router.get("/transacoes/{category}", status_code=200)
def transactions_category(category:str, session: SessionDep, Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    user = user_of_token(session, KEY, Authorization)
    if user:
        return session.exec(select(Transaction).where(Transaction.category == category, Transaction.user == user)).all()