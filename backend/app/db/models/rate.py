from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship, Session
from app.db.models import Base
from typing import Tuple, List


def attribute_mapper(l, atr='id'):
    """ Retrieves attribute value for each element in list or tuple """
    return [getattr(atr_l, atr) for atr_l in l]


class ExchangeHolder:
    """
    Holds queryset with prefetched exchange rates to be filtered later
    TODO: check if it lazy-loaded to prevent extra fetching
    """

    def __init__(self, queryset, cls, date_range):
        self.queryset = queryset
        self.cls = cls
        self.date_range = date_range

    def get_exchange(self, source, targets, date) -> List:
        """Returns target rates for source in form of dict"""
        # in_() is not yet supported for relationships in sqlalchemy

        if not date_range[0] < date < date_range[1]:
            assert False, 'Wrong date requested'

        targets_id = attribute_mapper(targets)
        sub_query = self.queryset.filter(
            (self.cls.source == source)
            & (self.cls.target_id.in_(targets_id))
            & (self.cls.date == date)
        )
        return [{"code": rate.target.code, "price": rate.rate} for rate in sub_query]


class ExchangeRates(Base):
    """
    Records of relations between 2 currencies on some date
    E.g. Exchange rate of RUB for USD on 08.05.2020 was 73.93
    """

    id = Column(Integer, primary_key=True)
    source_id = Column(String(3), ForeignKey('currency.id'), nullable=False)
    target_id = Column(String(3), ForeignKey('currency.id'), nullable=False)
    rate = Column(Numeric(precision=15, scale=5), nullable=False)  # 1234567890.12345
    date = Column(Date, nullable=False)

    source = relationship('Currency', foreign_keys=[source_id])
    target = relationship('Currency', foreign_keys=[target_id])

    def __repr__(self):
        return f'<ExchangeRates source={self.source.code} target={self.target.code} rate={self.rate}>'

    @classmethod
    def get_exchange_holder(
        cls, date_range: Tuple, currencies: Tuple, db: Session
    ) -> ExchangeHolder:
        start_date, end_date = date_range

        # in_() is not yet supported for relationships in sqlalchemy
        currencies_id = attribute_mapper(currencies)

        queryset = db.query(cls).filter(
            (cls.date.between(start_date, end_date))
            & (cls.source_id.in_(currencies_id))
            & (cls.target_id.in_(currencies_id))
        )

        return ExchangeHolder(queryset, cls, date_range)


# from app.db.models import *
# from app.db.database import *
# from app.db.models.rate import *
# ses = SessionLocal()
# import datetime
# s = datetime.datetime.now() - datetime.timedelta(days=4)
# e = datetime.datetime.now() - datetime.timedelta(days=1)
# date_range = (s, e)
# TODO Можно выгрузить не просто 2 даты, а допустим объект в котором будет range и крайние точки
# c = ses.query(Currency).all()
# e = ExchangeRates.get_exchange_holder(date_range=date_range, currencies=c, db=ses)

# source = ses.query(Currency).filter(Currency.code == "RUB").first()
# targetUSD = ses.query(Currency).filter(Currency.code == "USD").first()
# targetEUR = ses.query(Currency).filter(Currency.code == "EUR").first()
# targets = (targetUSD, targetEUR)
# e.get_exchange(source=source, targets=targets)
