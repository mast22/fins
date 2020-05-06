from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from fastapi.exceptions import HTTPException


class BaseUser(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: bool = False
    default_currency: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    password: str

    @validator('password')
    def password_length(cls, password):
        PASSWORD_LENGTH = 8
        if len(password) < PASSWORD_LENGTH:
            raise HTTPException(
                status_code=400, detail=f"Password must contain more than {PASSWORD_LENGTH} symbols."
            )
        return password
