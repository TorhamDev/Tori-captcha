from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self, status_code=None, detail=None, headers=None) -> None:
        self.status_code = 400
        self.detail = "User with this email already exists."


class InvalidEmailAddress(HTTPException):
    def __init__(self, status_code=None, detail=None, headers=None) -> None:
        self.status_code = 400
        self.detail = "User email is not a valid email."


class EmailOrPasswordInvalid(HTTPException):
    def __init__(self, status_code=None, detail=None, headers=None) -> None:
        self.status_code = 400
        self.detail = "Email or password is invalid."


class CaptchaIsExpiredOrInvalidID(HTTPException):
    def __init__(self, status_code=None, detail=None, headers=None) -> None:
        self.status_code = 404
        self.detail = "Invalid id. Maybe the captcha has expired."
