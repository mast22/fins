from sqlalchemy import Column, String, Integer, Numeric, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base
from sqlalchemy.orm import Session
from app.db.models.user import User

from operator import attrgetter
from itertools import groupby


class SavingsHolder:
    def __init__(self, queryset, cls):
        self.queryset = queryset
        self.cls = cls

    def get_date_range(self):
        pass

    def get_date_ends(self):
        pass

    def get_savings(self):
        pass


class Savings(Base):
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Numeric(precision=15, scale=2), nullable=False)
    currency_id = Column(String, ForeignKey('currency.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", foreign_keys=[user_id])
    currency = relationship("Currency", foreign_keys=[currency_id])

    def __repr__(self):
        return f"<Savings date={self.date} amount={self.amount} currency={self.currency.code}>"

    @classmethod
    def get_user_savings(cls, user: User, db: Session):
        queryset = (
            db.query(cls).filter(cls.user == user).order_by(cls.date.desc()).all()
        )
        return SavingsHolder(queryset, cls)

    # s.query(Savings).filter(Savings.user==u).order_by(Savings.date.desc()).all()
    # from operator import attrgetter
    # from itertools import groupby
    # l = [list(g) for k, g in groupby(r, attrgetter('date'))]
