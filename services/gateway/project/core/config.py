import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)
    secret: str = os.getenv("SECRET_KEY", "hello_precious")
    gateway_timeout: int = os.getenv("GATEWAY_TIMEOUT", 10)
    client_url: str = os.getenv("CLIENT_URL", "http://localhost:8001")
    admin_url: str = os.getenv("ADMIN_URL", "http://localhost:8002")
    recaptcha_secret: str = os.getenv("RECAPTCHA_SECRET")


@lru_cache
def get_settings() -> BaseSettings:
    return Settings()
