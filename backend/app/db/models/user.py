from sqlalchemy import Column, String, Integer, Numeric, Date, Boolean
from sqlalchemy.orm import Session
from app.db.database import Base
from app.auth.security import hash_pass, verify_pass
from app.schemas.users import UserCreate


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    @classmethod
    def get_user_by_email(cls, email: str, password: str, db: Session):
        user = db.query(cls).filter(cls.email == email).first()
        if user and verify_pass(password, user.password):
            return user
        return None

    @classmethod
    def get(cls, id: int, db: Session):
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def create_user(cls, user: UserCreate, db: Session):
        new_user = cls(email=user.email, password=hash_pass(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
