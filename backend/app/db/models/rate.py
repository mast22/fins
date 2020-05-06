from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class ExchangeRates(Base):
    id = Column(Integer, primary_key=True)
    source_id = Column(String(3), ForeignKey('currency.id'), nullable=False)
    target_id = Column(String(3), ForeignKey('currency.id'), nullable=False)
    rate = Column(Numeric(precision=15, scale=5), nullable=False)  # 1234567890.12345
    date = Column(Date, nullable=False)

    source = relationship('Currency', foreign_keys=[source_id])
    target = relationship('Currency', foreign_keys=[target_id])
