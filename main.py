from fastapi import FastAPI
from app.accounts.register import router as register_router

app = FastAPI()

app.include_router(register_router)


@app.get("/")
def root():
    return {"Hi": "Halo"}
