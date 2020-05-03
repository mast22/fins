from typing import Generator
from app.db.database import SessionLocal
from app.db.models.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from app.core.config import SECRET_KEY, ALGORITHM
from app.schemas.tokens import TokenPayload
from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt

oauth2 = OAuth2PasswordBearer(tokenUrl="/token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2)
) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(status_code=403, detail="Credentials cannot be validated")
    user = User.get(db=db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")

    return user
