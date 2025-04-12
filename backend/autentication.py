import jwt
from fastapi import FastAPI, Header, HTTPException, Depends, Security
from sqlmodel import Session, select
from models import *

def user_of_token(session, key, Authorization):
    bearer_token = Authorization.split(' ')
    if len(bearer_token) < 2:
        raise HTTPException(status_code=403, detail=f"Formato do authorization deve ser: Bearer token")
    try:
        token = bearer_token[1]
        token = jwt.decode(token, key, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=403, detail=f"Token inválido")
    
    existent_user = session.exec(select(User).where(User.email == token.get('email', ""))).first()

    if existent_user:
        return existent_user.id
    else:
        raise HTTPException(status_code=403, detail=f"Usuário inválido")