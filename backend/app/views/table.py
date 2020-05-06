from fastapi import APIRouter, Depends
from app.schemas.table import Table
from app.schemas.users import User as UserModel
from app.db.deps import get_current_user, get_db
from app.db.models.savings import Savings
from app.db.models.column import Column

router = APIRouter()


@router.get("/", response_model=Table)
def main_table(current_user: UserModel = Depends(get_current_user), db=Depends(get_db)):
    savings = Savings.get_user_savings(current_user, db)
    columns = Column.get_user_columns(current_user, db)
    date_range = (savings[0].date, savings[-1].date)
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
                        "code": "RUB",
                        "display": "ruble",
                        "amount": 1000,
                        "exchange": [
                            {"code": "EUR", "price": 85.23,},
                            {"code": "USD", "price": 75.23,},
                        ],
                    },
                    {
                        "code": "USD",
                        "display": "dollar",
                        "amount": 500.23,
                        "exchange": [
                            {"code": "RUB", "price": 0.012,},
                            {"code": "USD", "price": 1.12,},
                        ],
                    },
                    {
                        "code": "EUR",
                        "display": "euro",
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
