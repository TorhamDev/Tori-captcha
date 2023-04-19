from fastapi import APIRouter
from app.models import Users
from app.schema import UserCreate, UserDataResponse
from app.errors import UserAlreadyExists

router = APIRouter()


@router.post("/register")
def register(data: UserCreate) -> UserDataResponse:
    user = Users.select().where(Users.email == data.email)

    if user.exists():
        raise UserAlreadyExists

    user = Users(**dict(data))
    user.save()

    return data
