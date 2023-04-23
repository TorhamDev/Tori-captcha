from pydantic import BaseModel
from uuid import UUID


class CreateCaptchaResponse(BaseModel):
    id: UUID
