from fastapi import APIRouter
from app.captcha.captcha_tools import make_captcha_image
from app.database import redis_db
from app.utils import get_unique_id_for_redis, make_random_captcha_question
from app.schema import CreateCaptchaResponse


router = APIRouter()


@router.get("/create", response_model=CreateCaptchaResponse)
def create_captcha():

    question, answer = make_random_captcha_question()

    captcha_image = make_captcha_image(question)

    captcha_id = get_unique_id_for_redis()

    redis_db.set(captcha_id, str({"image": captcha_image, "answer": answer}))

    return {"id": captcha_id}
