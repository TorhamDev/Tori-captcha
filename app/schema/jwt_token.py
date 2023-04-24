from pydantic import BaseModel, EmailStr


class JwtTokensResponse(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    exp: int
    email: EmailStr
