from pydantic import EmailStr

from app.schema import UserLoginData
from app.errors import EmailOrPasswordInvalid
from app.models import Users
from app.utils import verify_password


def validate_user_by_email_and_password(
    email: EmailStr, password: str
) -> UserLoginData:
    """
    Validating user by email and verifing password

    return : UserLoginData -> email, password
    """
    user = Users.select().where(Users.email == email)

    if not user.exists():
        raise EmailOrPasswordInvalid

    user = user[0]

    password_is_correct: bool = verify_password(
        password,
        user.password,
    )

    if not password_is_correct:
        raise EmailOrPasswordInvalid

    return UserLoginData(email=user.email, password=user.password)
