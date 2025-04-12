import jwt
from fastapi import APIRouter, HTTPException, Depends
from models import *
from typing import Annotated
from sqlmodel import Session, select
from dependencies import get_session, KEY
from hashfunctions import get_password_hash, verify_password

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/registrar", status_code=201)
def create_user(user: UserCreate, session: SessionDep):

    # Verifica se o email já está no banco de dados
    select_user = select(User).where(User.email == user.email)
    existent_user = session.exec(select_user).all()

    if not existent_user:
        hashed_password = get_password_hash(user.password) # Faz hash da senha
        new_user = User(
            email = user.email,
            name = user.name,
            password = hashed_password,
            birthDate = user.birthDate
        )
        session.add(new_user) # cria novo user
        session.commit()
        session.refresh(new_user)

        # Cria jwt
        payload = {"email": new_user.email}
        encoded_jwt = jwt.encode(payload, KEY, algorithm="HS256")
        json_jwt = {"jwt": f"{encoded_jwt}"}
        return json_jwt
    else:
        # Se o email já está cadastrado
        raise HTTPException(status_code=409, detail=f"Email já cadastrado")
    
@router.get("/users", status_code=200)
def users(session: SessionDep):
    return session.exec(select(User)).all()

@router.post("/login", status_code=200)
def login(login: Login, session: SessionDep):
    # Busca usuário no banco de dados
    existent_user = session.scalar(select(User).where(User.email == login.email))

    if existent_user:
        hashed_password = existent_user.password
        if (verify_password(login.password, hashed_password)):
            payload = {"email" : existent_user.email}
            encoded_jwt = jwt.encode(payload, KEY, algorithm="HS256")
            json_jwt = {"jwt": f"{encoded_jwt}"}
            return json_jwt
        else:
            raise HTTPException(status_code=401, detail=f"Senha incorreta")
    else:
        raise HTTPException(status_code=401, detail=f"Usuário não cadastrado")