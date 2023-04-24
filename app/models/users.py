import peewee

from app.database import db


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
        to_field='setting_id',
    )

    class Meta:
        database = db


db.connect()
db.create_tables([Users, CaptchaSettings], safe=True)
db.close()
