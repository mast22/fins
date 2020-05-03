from argon2 import PasswordHasher
from datetime import datetime, timedelta
from app.core.config import JWT_EXPIRES_MINUTES, SECRET_KEY, ALGORITHM
from jose import jwt


def hash_pass(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def verify_pass(password: str, hash: str) -> bool:
    ph = PasswordHasher()
    return ph.verify(hash, password)


def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRES_MINUTES)

    to_encode = {'exp': expire, 'sub': str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
