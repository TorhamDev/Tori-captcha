from contextvars import ContextVar
from app.configs import REDIS_DB, REDIS_HOST, REDIS_PORT
import peewee
import redis

# redis database connection
redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


db_state_default = {
    "closed": None,
    "conn": None,
    "ctx": None,
    "transactions": None,
}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.SqliteDatabase('./app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64}
)
db._state = PeeweeConnectionState()
