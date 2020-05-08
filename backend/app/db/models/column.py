from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.query import Query
from app.db.models import Base

from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.currency import Currency
from app.core.utils import attribute_mapper

from typing import List


class ColumnHolder:
    def __init__(self, queryset: Query):
        self.queryset = queryset

    def get_columns(self):
        """Returnc dict columns"""
        columns = [
            {
                "id": column.id,
                "currency": column.currency.code,
                "color": column.color,
                "desc": column.desc,
            }
            for column in self.queryset
        ]
        return columns

    def get_currencies(self) -> List:
        return [column.currency for column in self.queryset]

    def get_currencies_against(self, currency: Currency) -> List[Currency]:
        """Get all user currencies except for choosen"""
        l = self.get_currencies()
        l.remove(currency)
        return l


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
    def get_user_columns_holder(cls, user: User, db: Session) -> ColumnHolder:
        queryset = db.query(cls).filter(cls.user == user).order_by(cls.order)
        return ColumnHolder(queryset)
