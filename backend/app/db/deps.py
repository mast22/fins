from typing import Generator
from app.db.database import SessionLocal
from app.db.models.user import User


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



