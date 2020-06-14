from sqlalchemy.ext.declarative import as_declarative, declared_attr
from typing import Any


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    # Generate __tablename__ automatically
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @declared_attr
    # # Generate __repr__ automatically
    def __repr__(cls) -> str:
        return f'<{cls.__name__}>'


from app.db.models.currency import Currency
from app.db.models.savings import Savings
from app.db.models.rate import ExchangeRates
from app.db.models.user import User
from app.db.models.saving_set import Column
