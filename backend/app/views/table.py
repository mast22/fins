from fastapi import APIRouter, Depends
from app.schemas.table import Table
from app.schemas.table import Column as ColumnSchema
from app.schemas.users import User as UserSchema
from app.db.deps import get_current_user, get_db
from app.db.models.savings import Savings
from app.db.models.savings import Column
from app.db.models.rate import ExchangeRates

router = APIRouter()


@router.get("/", response_model=Table)
def main_table(
    current_user: UserSchema = Depends(get_current_user), db=Depends(get_db)
):
    savings = Savings.get_user_savings(current_user, db)
    columns_holder = Column.get_user_columns_holder(current_user, db)
    date_range = (savings[0].date, savings[-1].date)
    exchange_holder = ExchangeRates.get_exchange_holder(date_range, db)

    response_columns = [
        {"currency": column.currency.code, "color": column.color, "desc": column.desc}
        for column in columns
    ]

    response_data = []

    for day in savings:
        currencies = []
        for currency in day:
            currencies.append(
                {
                    "id": currency.id,
                    "code": currency.code,
                    "amount": currency.amount,
                    "exchange": exchange_holder.get_exchange(
                        source=currency.code,
                        targets=columns.get_targets_against(currency=currency),
                    ),
                }
            )
        query_day = {"date": day.date, "currencies": currencies}
        response_data.append()

    # response = {"columns": response_columns, "data": response_data}

    # TODO доделать
    return {
        "columns": [
            {"currency": "RUB", "color": "8B0000", "desc": "Рублёвый счёт"},
            {"currency": "USD", "color": "059117", "desc": "Dollars"},
            {"currency": "EUR", "color": "0000FF", "desc": "Мою любымые евро"},
        ],
        "data": [
            {
                "date": "2020-05-01",
                "currencies": [
                    {
                        "id": "1",
                        "code": "RUB",
                        "amount": 1000,
                        "exchange": [
                            {"code": "EUR", "price": 85.23,},
                            {"code": "USD", "price": 75.23,},
                        ],
                    },
                    {
                        "id": "2",
                        "code": "USD",
                        "amount": 500.23,
                        "exchange": [
                            {"code": "RUB", "price": 0.012,},
                            {"code": "USD", "price": 1.12,},
                        ],
                    },
                    {
                        "id": "3",
                        "code": "EUR",
                        "amount": 200.23,
                        "exchange": [
                            {"code": "RUB", "price": 0.01,},
                            {"code": "EUR", "price": 0.89,},
                        ],
                    },
                ],
            },
        ],
    }
