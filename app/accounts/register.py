from fastapi import APIRouter
from app.models import Users
from app.schema import UserCreate, UserDataResponse
from app.errors import UserAlreadyExists

router = APIRouter()


@router.post("/register", response_model=UserDataResponse)
def register(data: UserCreate):

    user = Users.select().where(Users.email == data.email)

    if user.exists():
        raise UserAlreadyExists

    Users.create_new_user(data)

    return data
