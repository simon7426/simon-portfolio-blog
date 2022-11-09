from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from project.models import blogs


async def add_blog(data: dict, conn: AsyncIOMotorClient):
    return await conn.blogs["blogs"].insert_one(data)


async def get_blog(id: str, conn: AsyncIOMotorClient) -> blogs.Blog:
    blog: dict | None = await conn.blogs["blogs"].find_one({"_id": ObjectId(id)})
    if not blog:
        return None
    return blogs.Blog(**blog)


async def update_blog(id: str, data: dict, conn: AsyncIOMotorClient) -> blogs.Blog:
    return await conn.blogs["blogs"].replace_one({"_id": ObjectId(id)}, data)


async def delete_blog(id: str, conn: AsyncIOMotorClient):
    return await conn.blogs["blogs"].delete_one({"_id": ObjectId(id)})
