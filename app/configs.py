import os

# JWT configs
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ.get(
    'JWT_SECRET_KEY',
    "y*e6(ub(^4g@bkvgthivqfg3v%2xjbm&dlze-u7a5mu$@sk3p-"
)
JWT_REFRESH_SECRET_KEY = os.environ.get(
    'JWT_REFRESH_SECRET_KEY',
    "qed3jo@yvhaiofxbe)d8%*c4u(a71(!qow#msc8xjh+ju*uil="
)

# redis configs
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_DB = os.environ.get("REDIS_DB", 0)
