from fastapi import APIRouter

router = APIRouter()


@router.get("/account")
def user_page():
    return {'username': 'nick'}

