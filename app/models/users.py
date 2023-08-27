import peewee

from app.database import db
from app.schema import UserCreate
from app.utils import get_hashed_password


class CaptchaSettings(peewee.Model):
    setting_id = peewee.PrimaryKeyField()
    captcha_exp = peewee.BigIntegerField(default=60)  # base on second

    class Meta:
        database = db


class Users(peewee.Model):
    name = peewee.CharField(max_length=150)
    email = peewee.CharField(unique=True)
    password = peewee.CharField()
    captcha_settings = peewee.ForeignKeyField(
        CaptchaSettings,
        to_field="setting_id",
    )

    @classmethod
    def create_new_user(cls, user_data: UserCreate):
        user_data.password = get_hashed_password(user_data.password)
        user = Users(**dict(user_data))
        captcha_setting = CaptchaSettings().save()
        user.captcha_settings = captcha_setting
        user.save()

        return None

    class Meta:
        database = db


db.connect()
db.create_tables([Users, CaptchaSettings], safe=True)
db.close()
