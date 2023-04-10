from fastapi import FastAPI
from .login_and_register.register import router as register_router

app = FastAPI()

app.include_router(register_router)
