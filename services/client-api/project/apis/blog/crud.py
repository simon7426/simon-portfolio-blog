from datetime import datetime
from typing import Any, List

from bson import ObjectId

from project.apis.models import BlogCollection, CommentPost


async def get_all_blogs(tag: str, db: Any) -> List[BlogCollection]:
    query: dict = {}
    if len(tag):
        query = {"tags": {"$in": [tag]}}
    return await db["blogs"].find(query).to_list(1000)


async def get_blog(id: str, db: Any):
    return await db["blogs"].find_one({"_id": ObjectId(id)})


async def add_comment(id: str, data: CommentPost, db: Any):
    blog = await get_blog(id, db)
    data["_id"] = ObjectId()
    data["created_on"] = datetime.utcnow()
    if blog.get("comments") is None:
        blog["comments"] = []
    blog["comments"].append(data)
    return await db["blogs"].replace_one({"_id": ObjectId(id)}, blog)
