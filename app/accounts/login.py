from fastapi import APIRouter
from fastapi import Depends

from typing import Annotated

from app.schema import JwtTokensResponse, UserLoginData
from app.utils import create_jwt_token
from app.accounts.accounts_validation import validate_user_by_email_and_password

router = APIRouter()


@router.post("/login", response_model=JwtTokensResponse, tags=["accounts"])
def login(
    validated_user: Annotated[
        UserLoginData, Depends(validate_user_by_email_and_password)
    ],
):
    return JwtTokensResponse(
        access_token=create_jwt_token(validated_user.email),
        refresh_token=create_jwt_token(validated_user.email, is_refresh=True),
    )
