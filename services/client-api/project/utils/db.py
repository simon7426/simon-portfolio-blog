import logging

import motor.motor_asyncio

from project.config import Settings, get_settings
from project.utils import exceptions

logger = logging.getLogger("uvicorn")

db = None


def init_db():
    settings: Settings = get_settings()
    logger.info("Initializing Database")
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongo_uri)
    global db
    db = client.blogs


def get_db():
    if db is None:
        logger.error("Database is not initialized")
        raise exceptions.DBNotInitialized
    return db
