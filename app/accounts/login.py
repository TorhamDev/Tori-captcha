from fastapi import APIRouter
from app.models import Users
from app.schema import UserLoginData
from app.errors import EmailOrPasswordInvalid
from app.utils import verify_password

router = APIRouter()


@router.post("/login")
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

    return {"ok": "duok"}
