import os

APP_ENV = os.getenv("APP_ENV", "development")
APP_HOST = os.environ.get("APP_HOST", "127.0.0.1")
APP_DEBUG = os.environ.get("APP_DEBUG", "True")
APP_NAME = os.environ.get("APP_NAME", "JWT Authorization")
APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "JWT Authorization API")
APP_VERSION = os.environ.get("APP_VERSION", "0.0.1")

APP_ROUTE_PREFIX = os.environ.get("APP_ROUTE_PREFIX", "api")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 720)
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES", 1440)
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "75d1fc497cd4a7366cb3a1967af1daf1b38a2a23a7381038dd39729d34ff43ac") # Generate a 256-bit (32-byte) secret key
