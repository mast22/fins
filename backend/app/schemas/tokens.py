from typing import Optional
from pydantic import BaseModel


class TokenPayload(BaseModel):
    exp: str
    sub: Optional[int] = None


class Token(BaseModel):
    access_token: str
    token_type: str
