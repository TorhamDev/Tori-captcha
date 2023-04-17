import peewee

from app.database import db


class Users(peewee.Model):
    name = peewee.CharField(max_length=150)
    email = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users], safe=True)
db.close()
