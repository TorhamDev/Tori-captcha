from fastapi import APIRouter
from app.models import Users
from app.schema import UserCreate, UserDataResponse
from app.errors import UserAlreadyExists
from app.accounts.accounts_validation import Checking_existence_user

router = APIRouter()


@router.post("/register", response_model=UserDataResponse, tags=["accounts"])
def register(user_data: UserCreate):
    if not Checking_existence_user:
        raise UserAlreadyExists

    Users.create_new_user(user_data)

    return user_data
