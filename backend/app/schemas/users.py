from pydantic import BaseModel, EmailStr

from typing import Optional


class User(BaseModel):
    id: int
    email: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str
