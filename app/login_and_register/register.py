from fastapi import APIRouter

router = APIRouter()


@router.get("/register")
def user_register():

    return {"register": 1}


@router.get("/login")
def user_login():

    return {"login": 1}
