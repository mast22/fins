from pydantic import BaseModel, EmailStr

from typing import Optional


class BaseUser(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: bool = False


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    password: str
