from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base

from sqlalchemy.orm import Session
from app.db.models.user import User


class Column(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    currency_id = Column(ForeignKey("currency.id"))
    desc = Column(String(30))
    order = Column(Integer)
    color = Column(String(6))

    user = relationship("User")
    currency = relationship("Currency")

    def __repr__(self):
        return f'<Column user={self.user.id} currency={self.currency.code}>'

    @classmethod
    def get_user_columns(cls, user: User, db: Session):
        return db.query(cls).filter(cls.user == user).order_by(cls.order)
