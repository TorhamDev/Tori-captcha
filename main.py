from fastapi import FastAPI
from app.accounts.register import router as register_router
from app.accounts.login import router as login_router

app = FastAPI()

app.include_router(register_router)
app.include_router(login_router)


@app.get("/")
def root():
    return {"Hi": "Halo"}
