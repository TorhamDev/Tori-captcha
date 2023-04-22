from pydantic import BaseModel, UUID4


class CreateCaptchaResponse(BaseModel):
    id: UUID4
