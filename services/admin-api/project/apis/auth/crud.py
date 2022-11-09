from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from project.models import users


async def add_user(data: dict, conn: AsyncIOMotorClient):
    return await conn.blogs["users"].insert_one(data)


async def get_user(id: str, conn: AsyncIOMotorClient):
    user: dict = await conn.blogs["users"].find_one({"_id": ObjectId(id)})
    if not user:
        return None
    return users.User(**user)


async def get_user_by_username(username: str, conn: AsyncIOMotorClient):
    user: dict = await conn.blogs["users"].find_one({"username": username})
    if not user:
        return None
    return users.User(**user)
