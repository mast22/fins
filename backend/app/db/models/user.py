from sqlalchemy import Column, String, Integer, Numeric, Date

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    password = Column(Integer)

    @classmethod
    def get_user_by_email(cls, email: str, db: Session):
        return db.query(cls).filter(cls.email == email).first()

class ExchangeRates(Base):
    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True)
    source = Column(String(3), nullable=False)
    target = Column(String(3), nullable=False)
    rate = Column(Numeric(precision=15, scale=5), nullable=False)  # 1234567890.12345
    date = Column(Date, nullable=False)
