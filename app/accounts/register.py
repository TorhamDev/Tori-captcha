from fastapi import APIRouter, HTTPException
from app.models import Users
from app.schema import UserCreate, UserDataResponse

router = APIRouter()


@router.post("/register")
def register(data: UserCreate) -> UserDataResponse:
    user = Users.select().where(Users.email == data.email)

    if user.exists():
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    user = Users(**dict(data))
    user.save()

    return data
