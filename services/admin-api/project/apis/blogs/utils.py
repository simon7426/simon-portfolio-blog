from datetime import datetime

from fastapi import status
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.exceptions import HTTPException

from project.apis.blogs import crud
from project.models import blogs


async def add_blog_handler(data: dict, conn: AsyncIOMotorClient) -> blogs.Blog:
    data["created_at"] = datetime.utcnow()
    data["updated_at"] = None
    data["comments"] = []
    response = await crud.add_blog(data, conn)
    blog = await crud.get_blog(str(response.inserted_id), conn)
    return blog


async def update_blog_handler(
    id: str, data: dict, conn: AsyncIOMotorClient
) -> blogs.Blog:
    blog: blogs.Blog | None = await crud.get_blog(str(id), conn)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog {str(id)} does not exists.",
        )
    blog.title = data["title"]
    blog.body = data["body"]
    blog.tags = data["tags"]
    blog.updated_at = datetime.utcnow()
    _ = await crud.update_blog(id, blog.dict(), conn)
    return await crud.get_blog(id, conn)


async def delete_blog_handler(id: str, conn: AsyncIOMotorClient):
    blog: blogs.Blog | None = await crud.get_blog(str(id), conn)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog {str(id)} does not exists.",
        )

    _ = await crud.delete_blog(id, conn)


async def delete_comment_handler(
    blog_id: str, comment_id: str, conn: AsyncIOMotorClient
):
    blog: blogs.Blog | None = await crud.get_blog(str(blog_id), conn)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog {str(blog_id)} does not exists",
        )
    found = False
    for comment in blog.comments:
        if comment["_id"] == comment_id:
            found = True
            blog.comments.remove(comment)
            break
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment {str(comment_id)} does not exists",
        )
    blog.updated_at = datetime.utcnow()
    _ = await crud.update_blog(blog_id, blog.dict(), conn)
    return await crud.get_blog(blog_id, conn)
