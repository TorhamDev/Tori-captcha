from pydantic import BaseModel
from uuid import UUID


class CreateCaptchaResponse(BaseModel):
    id: UUID


class CaptchaCheckAnswer(BaseModel):
    is_correct: bool
