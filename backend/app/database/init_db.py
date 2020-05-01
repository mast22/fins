import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, ExchangeRates
from session import Session, engine
from db_config import db_path, sqlite_db_path


def main(populate=False):

    try:
        # удаляем если существует
        os.remove(db_path)
    except:
        pass

    engine = create_engine(sqlite_db_path, echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    if populate:
        session = Session()

        session.add_all(
            [
                ExchangeRates(
                    source='EURO',
                    target='USD',
                    rate=1.090000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='EURO',
                    target='USD',
                    rate=1.100000,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='EURO',
                    target='USD',
                    rate=1.080000,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='EURO',
                    target='USD',
                    rate=1.110000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source='USD',
                    target='EURO',
                    rate=0.910000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='USD',
                    target='EURO',
                    rate=0.923651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='USD',
                    target='EURO',
                    rate=0.906452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='USD',
                    target='EURO',
                    rate=0.930000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source='RUB',
                    target='USD',
                    rate=0.013000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='RUB',
                    target='USD',
                    rate=0.014651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='RUB',
                    target='USD',
                    rate=0.013452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='RUB',
                    target='USD',
                    rate=0.013000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source='USD',
                    target='RUB',
                    rate=74.800000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='USD',
                    target='RUB',
                    rate=74.793651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='USD',
                    target='RUB',
                    rate=74.806452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='USD',
                    target='RUB',
                    rate=75.100000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source='RUB',
                    target='EURO',
                    rate=0.012000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='RUB',
                    target='EURO',
                    rate=0.012651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='RUB',
                    target='EURO',
                    rate=0.012452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='RUB',
                    target='EURO',
                    rate=0.013000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
                ExchangeRates(
                    source='EURO',
                    target='RUB',
                    rate=81.690000,
                    date=datetime.datetime.now(),
                ),
                ExchangeRates(
                    source='EURO',
                    target='RUB',
                    rate=81.793651,
                    date=datetime.datetime.now() - datetime.timedelta(days=1),
                ),
                ExchangeRates(
                    source='EURO',
                    target='RUB',
                    rate=81.806452,
                    date=datetime.datetime.now() - datetime.timedelta(days=2),
                ),
                ExchangeRates(
                    source='EURO',
                    target='RUB',
                    rate=81.930000,
                    date=datetime.datetime.now() - datetime.timedelta(days=3),
                ),
            ]
        )
        session.commit()


if __name__ == '__main__':
    import sys

    main(populate=(sys.argv[1] == 'pop'))
