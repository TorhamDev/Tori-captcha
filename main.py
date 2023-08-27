from fastapi import FastAPI
from app.accounts.register import router as register_router
from app.accounts.login import router as login_router
from app.captcha.captcha_apis import router as captcha_router

app = FastAPI(
    title="Tori Captcha",
    description="A captcha system",
    version="0.0.1",
)

app.include_router(register_router)
app.include_router(login_router)
app.include_router(captcha_router)


@app.get("/", tags=["root"])
def root():
    return {"Hi": "Halo"}
