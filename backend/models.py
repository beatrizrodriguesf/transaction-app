from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key=True) 
    name: str
    email: str
    password: str
    birthDate: datetime.date

class Login(SQLModel):
    email: str
    password: str

class Transaction(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key=True)
    type: str # receita ou despesa
    value: float
    date: datetime.date
    category: str = Field(foreign_key="category.name")
    user: int = Field(foreign_key="category.id")
    details: Optional[str]

class Category(SQLModel, table = True):
    name: str = Field(primary_key=True)
    user: int = Field(foreign_key="category.id")
    details: str

class CommonHeaders(BaseModel):
    jwt: str