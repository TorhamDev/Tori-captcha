from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from uuid import uuid4, UUID
from random import randint, choice
from fastapi import HTTPException, status
from pydantic import ValidationError

from ast import literal_eval
from app.schema import TokenPayload
from app.database import redis_db
from app.errors import CaptchaIsExpiredOrInvalidID
from app.configs import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    JWT_REFRESH_SECRET_KEY,
)


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_jwt_token(user_email: str, is_refresh: bool = False) -> str:
    expire_time = (
        REFRESH_TOKEN_EXPIRE_MINUTES if is_refresh else ACCESS_TOKEN_EXPIRE_MINUTES
    )
    secret_key = JWT_REFRESH_SECRET_KEY if is_refresh else JWT_SECRET_KEY
    
    expires_delta = datetime.utcnow() + timedelta(minutes=expire_time)

    to_encode = {"exp": expires_delta, "email": user_email}
    encoded_jwt = jwt.encode(to_encode, secret_key, ALGORITHM)
    return encoded_jwt


def get_unique_id_for_redis() -> str:
    while True:
        uuid = str(uuid4())
        uuid_is_exists = redis_db.get(uuid)
        if uuid_is_exists:
            continue

        return uuid


def make_random_captcha_question():
    int_one = randint(0, 99)
    int_two = randint(0, 99)
    answer = int
    question_string = str

    oprator = choice(["-", "+", "x"])

    match oprator:
        case "-":
            question_string = f"{int_one} - {int_two}"
            answer = int_one - int_two
        case "+":
            question_string = f"{int_one} + {int_two}"
            answer = int_one + int_two
        case "x":
            question_string = f"{int_one} x {int_two}"
            answer = int_one * int_two

    return question_string, answer


def check_user_auth(jwt_token: str) -> TokenPayload:
    try:
        payload = jwt.decode(jwt_token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_data


def get_captcha_from_redis(captcha_id: UUID) -> dict:
    captcha_in_redis = redis_db.get(str(captcha_id))

    if captcha_in_redis is None:
        raise CaptchaIsExpiredOrInvalidID

    captcha_data = literal_eval(captcha_in_redis.decode())

    return captcha_data
