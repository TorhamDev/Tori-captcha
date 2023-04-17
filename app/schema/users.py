from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserDataResponse(BaseModel):
    name: str
    email: str
