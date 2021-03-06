import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from app.db.models import Base

from app.db.models.currency import Currency
from app.db.models.savings import Savings
from app.db.models.rate import ExchangeRates
from app.db.models.user import User
from app.db.models.saving_set import SavingsSet

from app.auth.security import hash_pass
from app.db.database import SessionLocal, engine
from app.core.config import SQLITE
import random


def main(populate=False):
    """
    Sometimes you just want to start over without dealing with migrations
    Drop your db, recreate it, populate with data
    """

    if SQLITE:
        # in case its sqlite based we import path and db_path with sqlite prefix
        from app.core.config import location, db_path

        # try:
        # remove if exist
        os.remove(location)
        # except:
        #     print('Disconnect database')
    else:
        # if its postgres then we connect to it
        from app.core.config import db_path

        # TODO remove postgres db and recreate it

    engine = create_engine(db_path, echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    if populate:
        session = SessionLocal()

        RUB = Currency(code='RUB')
        EUR = Currency(code='EUR')
        USD = Currency(code='USD')
        currencies = [RUB, EUR, USD]

        session.add_all(currencies)

        user1 = User(email='testemail@mail.com', password=hash_pass('password'))
        user2 = User(email='testemail2@mail.com', password=hash_pass('password2'))
        users = [user1, user2]

        session.add_all(users)

        savings = []

        for days in range(3):
            for cur in currencies:
                for user in users:
                    date = datetime.datetime.now() - datetime.timedelta(days=days)
                    amount = random.randint(1000, 500000) / 100

                    savings.append(
                        Savings(date=date, amount=amount, user=user, currency=cur)
                    )

        session.add_all(savings)

        columns = [
            SavingsSet(
                currency=RUB,
                user=user1,
                desc='Рублёвый счёт',
                order=1,
                color='8B0000',
            ),
            SavingsSet(currency=EUR, user=user1, desc='Euro', order=2, color='0000FF'),
            SavingsSet(
                currency=USD,
                user=user1,
                desc='$$$$$$$$$$$$$$$$$$$$$',
                order=3,
                color='059117',
            ),
            SavingsSet(currency=RUB, user=user2, desc='Рубли', order=1, color='8B0000'),
            SavingsSet(
                currency=USD,
                user=user2,
                desc='Рублёвый счёт',
                order=2,
                color='059117',
            ),
        ]

        session.add_all(columns)

        session.add_all(
            [
                ExchangeRates(
                    source=EUR, target=USD, rate=1.090000, date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=EUR,
                    target=USD,
                    rate=1.100000,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=EUR,
                    target=USD,
                    rate=1.080000,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=EUR,
                    target=USD,
                    rate=1.110000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source=USD, target=EUR, rate=0.910000, date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=USD,
                    target=EUR,
                    rate=0.923651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=USD,
                    target=EUR,
                    rate=0.906452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=USD,
                    target=EUR,
                    rate=0.930000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source=RUB, target=USD, rate=0.013000, date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=RUB,
                    target=USD,
                    rate=0.014651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=RUB,
                    target=USD,
                    rate=0.013452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=RUB,
                    target=USD,
                    rate=0.013000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source=USD,
                    target=RUB,
                    rate=74.800000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=USD,
                    target=RUB,
                    rate=74.793651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=USD,
                    target=RUB,
                    rate=74.806452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=USD,
                    target=RUB,
                    rate=75.100000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source=RUB, target=EUR, rate=0.012000, date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=RUB,
                    target=EUR,
                    rate=0.012651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=RUB,
                    target=EUR,
                    rate=0.012452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=RUB,
                    target=EUR,
                    rate=0.013000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source=EUR,
                    target=RUB,
                    rate=81.690000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source=EUR,
                    target=RUB,
                    rate=81.793651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source=EUR,
                    target=RUB,
                    rate=81.806452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source=EUR,
                    target=RUB,
                    rate=81.930000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
            ]
        )

        session.commit()


if __name__ == "__main__":
    main(populate=True)
