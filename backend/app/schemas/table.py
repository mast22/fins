from typing import List, Dict
from datetime import date
from decimal import Decimal
from pydantic import BaseModel


class Exchange(BaseModel):
    code: str
    price: float


class Currency(BaseModel):
    code: str
    display: str
    amount: float
    exchange: List[Exchange]


class Day(BaseModel):
    date: str
    currencies: List[Currency]


class Table(BaseModel):
    data: List[Day]


# {
#     "data": [
#         {
#             "date": "2020-05-01",
#             "currencies": [
#                 {
#                     "code": "RUB",
#                     "display": "ruble",
#                     "amount": 1000,
#                     "exchange": [
#                         {"code": "EUR", "price": 85.23,},
#                         {"code": "USD", "price": 75.23,},
#                     ],
#                 },
#                 {
#                     "code": "USD",
#                     "display": "dollar",
#                     "amount": 500.23,
#                     "exchange": [
#                         {"code": "RUB", "price": 0.012,},
#                         {"code": "USD", "price": 1.12,},
#                     ],
#                 },
#                 {
#                     "code": "EUR",
#                     "display": "euro",
#                     "amount": 200.23,
#                     "exchange": [
#                         {"code": "RUB", "price": 0.01,},
#                         {"code": "EUR", "price": 0.89,},
#                     ],
#                 },
#             ],
#         },
#     ],
# }
