from fastapi import APIRouter
from app.models import Users
from app.schema import UserCreate, UserDataResponse

router = APIRouter()


@router.post("/register")
def register(data: UserCreate) -> UserDataResponse:
    user = Users(**dict(data))
    user.save()
    return data
