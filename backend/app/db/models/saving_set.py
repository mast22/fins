from typing import List

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.orm.query import Query

from app.db.models import Base
from app.db.models.currency import Currency
from app.db.models.user import User


class SavingsSetHolder:
    def __init__(self, queryset: Query):
        self.queryset = queryset

    def get_savings_sets(self):
        """Returnc dict columns"""
        savings_sets = [
            {
                "id": saving_set.id,
                "currency": saving_set.currency.code,
                "color": saving_set.color,
                "desc": saving_set.desc,
            }
            for saving_set in self.queryset
        ]
        return savings_sets

    def get_currencies(self) -> List:
        return [saving_set.currency for saving_set in self.queryset]

    def get_currencies_against(self, currency: Currency) -> List[Currency]:
        """Get all user currencies except for choosen"""
        l = self.get_currencies()
        l.remove(currency)
        return l


class SavingsSet(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    currency_id = Column(ForeignKey("currency.id"))
    desc = Column(String(30))
    order = Column(Integer)
    color = Column(String(6))

    user = relationship("User")
    currency = relationship("Currency")

    def __repr__(self):
        return f'<SavingsSet user={self.user.id} currency={self.currency.code}>'

    @classmethod
    def get_user_savings_sets_holder(cls, user: User, db: Session) -> SavingsSetHolder:
        queryset = db.query(cls).filter(cls.user == user).order_by(cls.order)
        return SavingsSetHolder(queryset)
