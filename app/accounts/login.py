from fastapi import APIRouter
from app.models import Users
from app.schema import UserLoginData, JwtTokensResponse
from app.errors import EmailOrPasswordInvalid
from app.utils import verify_password, create_jwt_token

router = APIRouter()


@router.post("/login", response_model=JwtTokensResponse)
def login(data: UserLoginData):

    user = Users.select().where(Users.email == data.email)

    if not user.exists():
        raise EmailOrPasswordInvalid

    password_is_correct = verify_password(
        data.password,
        user[0].password,
    )

    if not password_is_correct:
        raise EmailOrPasswordInvalid

    return {
        "access_token": create_jwt_token(data.email),
        "refresh_token": create_jwt_token(data.email, is_refresh=True),
    }
