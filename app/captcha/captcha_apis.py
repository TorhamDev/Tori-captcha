from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.captcha.captcha_tools import make_captcha_image
from app.database import redis_db
from app.utils import get_unique_id_for_redis, make_random_captcha_question, check_user_auth
from app.schema import CreateCaptchaResponse
from ast import literal_eval
from io import BytesIO
from uuid import UUID
from fastapi import Security
from fastapi.security import APIKeyHeader


router = APIRouter()


@router.get("/create", response_model=CreateCaptchaResponse)
def create_captcha(jwt_token=Security(APIKeyHeader(name="X-API-Key"))):

    check_user_auth(jwt_token)

    question, answer = make_random_captcha_question()

    captcha_image = make_captcha_image(question)

    captcha_id = get_unique_id_for_redis()

    redis_db.set(captcha_id, str({"image": captcha_image, "answer": answer}))

    return {"id": captcha_id}


@router.get("/get-captcha/{captcha_id}/", response_class=StreamingResponse)
def get_captcha(captcha_id: UUID, jwt_token=Security(APIKeyHeader(name="X-API-Key"))):

    check_user_auth(jwt_token)

    captcha_in_redis = redis_db.get(str(captcha_id))
    captcha_data = literal_eval(captcha_in_redis.decode())

    headers = {
        'Content-Disposition': 'attachment; filename="captcha.png"',
    }
    return StreamingResponse(BytesIO(captcha_data["image"]), headers=headers, media_type="image/png")
