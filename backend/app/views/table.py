from fastapi import APIRouter, Depends
from app.schemas.users import User as UserSchema
from app.schemas.table import TablePost
from app.db.deps import get_current_user, get_db
from app.db.models.savings import Savings
from app.db.models.column import Column
from app.db.models.rate import ExchangeRates
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

router = APIRouter()


@router.get("/")
def main_table(
    current_user: UserSchema = Depends(get_current_user), db=Depends(get_db)
):
    savings_holder = Savings.get_user_savings_holder(current_user, db)
    columns_holder = Column.get_user_columns_holder(current_user, db)
    exchange_holder = ExchangeRates.get_exchange_holder(
        savings_holder.get_date_ends(), columns_holder.get_currencies(), db
    )

    response_data = []

    for day in savings_holder.get_savings():
        savings = []
        for saving in day:
            savings.append(
                {
                    "id": saving.id,
                    "code": saving.currency.code,
                    "amount": saving.amount,
                    "exchange": exchange_holder.get_exchange(
                        date=saving.date,
                        source=saving.currency,
                        targets=columns_holder.get_currencies_against(
                            currency=saving.currency
                        ),
                    ),
                }
            )
        response_data.append({"date": saving.date, "savings": savings})

    response = {"columns": columns_holder.get_columns(), "data": response_data}

    return response


@router.post("/")
def change_main_table(
    *,
    current_user: UserSchema = Depends(get_current_user),
    db=Depends(get_db),
    data: TablePost,
):
    try:
        Savings.update_savings(db=db, savings=data.dict()['savings'])
    except Exception as e:
        raise HTTPException(status_code=400, detail={'error': repr(e)})

    return {'detail': 'Ok!'}

    # {
    #     "columns": [
    #         {'id': 1, 'color': '235563', 'desc': 'new description'},
    #         {'id': 2, 'color': '235563', 'desc': 'new description'},
    #     ],
    #     "savings": [{"id": 1, "amount": 1234,}, {"id": 2, "amount": 1234.23,},],
    # }
