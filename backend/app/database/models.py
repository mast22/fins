from sqlalchemy import Column, String, Integer, Numeric, Date
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class ExchangeRates(Base):
    id = Column(Integer, primary_key=True)
    source = Column(String(3), nullable=False)
    target = Column(String(3), nullable=False)
    rate = Column(Numeric(precision=15, scale=5), nullable=False)  # 1234567890.12345
    date = Column(Date, nullable=False)
