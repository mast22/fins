from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.db.models.user import User as UserModel
from app.auth.security import hash_pass, verify_pass, create_access_token
from app.db.deps import get_db, oauth2, get_current_user
from app.schemas import users
from app.schemas import tokens


router = APIRouter()


@router.post('/', response_model=users.User)
def user_page(user: users.UserCreate, db=Depends(get_db)):
    new_user = UserModel.create_user(user, db)

    return new_user


@router.post('/token', response_model=tokens.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db),
):
    user = UserModel.get_user_by_email(
        email=form_data.username, password=form_data.password, db=db
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect password or username")

    access_token = create_access_token(user.id)

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me', response_model=users.User)
def my_account(current_user: UserModel = Depends(get_current_user)):
    return current_user
