from fastapi import APIRouter
from app.captcha.captcha_tools import make_captcha_image

router = APIRouter()


@router.get("/create")
def create_captcha():

    captcha_image = make_captcha_image("2+2")

    return {"test": "tst"}
