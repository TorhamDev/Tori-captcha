from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
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


def create_jwt_token(user_email: str, expires_delta: int = None, is_refresh: bool = False) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        if is_refresh:
            # using refresh expire time (longer time)
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "email": user_email}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt
