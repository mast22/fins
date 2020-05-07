from typing import List, Dict
from datetime import date
from decimal import Decimal
from pydantic import BaseModel


class Exchange(BaseModel):
    code: str
    price: float


class Currency(BaseModel):
    code: str
    amount: float
    exchange: List[Exchange]


class Day(BaseModel):
    date: str
    currencies: List[Currency]


class Column(BaseModel):
    currency: str
    color: str
    desc: str

    class Config:
        orm_mode = True


class Table(BaseModel):
    data: List[Day]
    columns: List[Column]
