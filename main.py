from fastapi import FastAPI
from random import randint
from captcha_tools.make_image import make_captcha_image


app = FastAPI()


@app.get("/make")
def read_root():
    first = randint(10, 99)
    second = randint(10, 99)

    make_captcha_image(f"{first} + {second}")

    return {"make": True}
