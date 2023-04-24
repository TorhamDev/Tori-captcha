from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserDataResponse(BaseModel):
    name: str
    email: EmailStr


class UserLoginData(BaseModel):
    email: EmailStr
    password: str
