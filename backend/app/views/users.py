from fastapi import APIRouter, Depends


from app.db.models.user import User
from app.auth.security import hash_pass, verify_pass
from app.db.deps import get_db
from app.schemas import users


router = APIRouter()


@router.post('/create')
def user_page(user: users.UserCreate, db=Depends(get_db)):
    return {'123': print(db)}
