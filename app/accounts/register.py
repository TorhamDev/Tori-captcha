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

    data.password = get_hashed_password(data.password)
    user = Users(**dict(data))
    captcha_setting = CaptchaSettings().save()
    user.captcha_settings = captcha_setting
    user.save()

    return data
