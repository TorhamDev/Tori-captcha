from fastapi import APIRouter
from app.models import Users
from app.schema import UserCreate, UserDataResponse
from app.errors import UserAlreadyExists
from app.validations import validate_email
from hashlib import sha256

router = APIRouter()


@router.post("/register")
def register(data: UserCreate) -> UserDataResponse:

    user = Users.select().where(Users.email == data.email)

    if user.exists():
        raise UserAlreadyExists

    password = sha256()
    password.update(data.password.encode())
    data.password = password.hexdigest()
    user = Users(**dict(data))
    user.save()

    return data
