from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self, status_code=None, detail=None, headers=None) -> None:
        self.status_code = 400
        self.detail = "User with this email already exists."
