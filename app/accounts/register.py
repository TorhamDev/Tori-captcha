from fastapi import APIRouter
from app.models import Users, CaptchaSettings
from app.schema import UserCreate, UserDataResponse
from app.errors import UserAlreadyExists
from app.utils import get_hashed_password

router = APIRouter()


@router.post("/register", response_model=UserDataResponse)
def register(data: UserCreate):

    user = Users.select().where(Users.email == data.email)

    if user.exists():
        raise UserAlreadyExists

    Users.create_new_user(data)

    return data
