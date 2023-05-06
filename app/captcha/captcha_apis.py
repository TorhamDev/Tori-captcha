from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.captcha.captcha_tools import make_captcha_image
from app.database import redis_db
from app.utils import (
    get_unique_id_for_redis,
    make_random_captcha_question,
    check_user_auth,
    get_captcha_from_redis,
)
from app.schema import CreateCaptchaResponse, CaptchaCheckAnswer
from io import BytesIO
from uuid import UUID
from fastapi import Security
from fastapi.security import APIKeyHeader
from app.models import Users


router = APIRouter()


@router.get("/create", response_model=CreateCaptchaResponse, tags=["captcha"])
def create_captcha(jwt_token=Security(APIKeyHeader(name="X-API-Key"))):

    user_token = check_user_auth(jwt_token)
    user_obj = Users.select().where(Users.email == user_token.email)[0]

    question, answer = make_random_captcha_question()

    captcha_image = make_captcha_image(question)

    captcha_id = get_unique_id_for_redis()

    redis_db.set(captcha_id, str({"image": captcha_image, "answer": answer}))
    captcha_exp_time = user_obj.captcha_settings.captcha_exp
    redis_db.expire(captcha_id, captcha_exp_time)

    return {"id": captcha_id}


@router.get("/get-captcha/{captcha_id}/", response_class=StreamingResponse, tags=["captcha"])
def get_captcha(captcha_id: UUID, jwt_token=Security(APIKeyHeader(name="X-API-Key"))):

    check_user_auth(jwt_token)

    captcha_data = get_captcha_from_redis(captcha_id)

    headers = {
        'Content-Disposition': 'attachment; filename="captcha.png"',
    }
    return StreamingResponse(BytesIO(captcha_data["image"]), headers=headers, media_type="image/png")


@router.get("/get-answer/{captcha_id}/{answer}/", response_model=CaptchaCheckAnswer, tags=["captcha"])
def get_captcha_answer(captcha_id: UUID, answer: int, jwt_token=Security(APIKeyHeader(name="X-API-Key"))):

    check_user_auth(jwt_token)

    captcha_data = get_captcha_from_redis(captcha_id)

    if captcha_data["answer"] == answer:
        return {"is_correct": True}

    return {"is_correct": False}
