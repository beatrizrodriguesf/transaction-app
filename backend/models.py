from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional
from pydantic import BaseModel
from enum import Enum

class TransactionType(Enum):
    REVENUE = "revenue"
    EXPENSE = "expense"

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

class TransactionCreate(BaseModel):
    id: Optional[int] = Field(default = None, primary_key=True)
    type: TransactionType
    value: float
    date: date
    category: str = Field(foreign_key="category.name")
    user: int = Field(foreign_key="user.id")
    details: Optional[str]

class Transaction(TransactionCreate, SQLModel, table = True):
    pass

class Category(SQLModel, table = True):
    id: int = Field(primary_key=True)
    name: str
    user: int = Field(foreign_key="user.id")
    details: str

class CommonHeaders(BaseModel):
    jwt: str