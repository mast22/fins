from sqlalchemy import Column, String, Integer, Numeric, Date

from app.db.database import Base


class ExchangeRates(Base):
    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True)
    source = Column(String(3), nullable=False)
    target = Column(String(3), nullable=False)
    rate = Column(Numeric(precision=15, scale=5), nullable=False)  # 1234567890.12345
    date = Column(Date, nullable=False)
