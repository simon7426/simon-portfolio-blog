import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)
    mongo_uri: AnyUrl = os.getenv(
        "MONGO_URI", "mongodb://admin:johncena@localhost:27017/blogs?authSource=admin"
    )


@lru_cache
def get_settings() -> BaseSettings:
    return Settings()
