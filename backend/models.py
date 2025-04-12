from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    id: Optional[int] = Field(default = None, primary_key=True) 
    name: str
    email: str
    password: str
    birthDate: date

class User(UserCreate, SQLModel, table = True):
    pass

class Login(SQLModel):
    email: str
    password: str

class Transaction(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key=True)
    type: str # receita ou despesa
    value: float
    date: date
    category: str = Field(foreign_key="category.name")
    user: int = Field(foreign_key="user.id")
    details: Optional[str]

class Category(SQLModel, table = True):
    name: str = Field(primary_key=True)
    user: int = Field(foreign_key="user.id")
    details: str

class CommonHeaders(BaseModel):
    jwt: str