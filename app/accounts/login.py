from fastapi import APIRouter

from app.schema import JwtTokensResponse, UserLoginData
from app.utils import create_jwt_token
from app.accounts.accounts_validation import verify_user_pass

router = APIRouter()


@router.post("/login", response_model=JwtTokensResponse, tags=["accounts"])
def login(user_data: UserLoginData):
    validated_user = verify_user_pass(
        email=user_data.email, password=user_data.password
    )
    return JwtTokensResponse(
        access_token=create_jwt_token(validated_user.email),
        refresh_token=create_jwt_token(validated_user.email, is_refresh=True),
    )
