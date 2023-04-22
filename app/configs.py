import os

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
