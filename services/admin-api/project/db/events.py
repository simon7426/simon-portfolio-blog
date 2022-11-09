from motor.motor_asyncio import AsyncIOMotorClient

from project.core import config
from project.core.logging import logger
from project.db import mongodb


async def connect_to_database():
    logger.info("Connecting to Database")
    mongodb.db.client = AsyncIOMotorClient(str(config.get_settings().mongo_uri))
    logger.info("Connection to database is successful!")


async def destroy_database_connection():
    logger.info("Closing database connection")
    mongodb.db.client.close()
    logger.info("Database connection closed successfully.")
