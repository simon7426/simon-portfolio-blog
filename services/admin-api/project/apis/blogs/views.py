from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

from project.apis.blogs import utils
from project.db import mongodb
from project.models import blogs

router = APIRouter(prefix="/api/v1/admin/blogs")


@router.post("", response_model=blogs.Blog, status_code=status.HTTP_201_CREATED)
async def add_blog(data: blogs.BlogIn, conn=Depends(mongodb.get_database)):
    post_data: dict = jsonable_encoder(data)
    blog: blogs.Blog = await utils.add_blog_handler(post_data, conn)
    return blog


@router.put("/{id}", response_model=blogs.Blog)
async def update_blog(
    id: blogs.PyObjectId, data: blogs.BlogIn, conn=Depends(mongodb.get_database)
):
    put_data: dict = jsonable_encoder(data)
    blog: blogs.Blog = await utils.update_blog_handler(id, put_data, conn)
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: blogs.PyObjectId, conn=Depends(mongodb.get_database)):
    _ = await utils.delete_blog_handler(id, conn)
    return ""


@router.delete("/{blog_id}/comment/{comment_id}", status_code=status.HTTP_200_OK)
async def delete_comment(
    blog_id: blogs.PyObjectId,
    comment_id: blogs.PyObjectId,
    conn=Depends(mongodb.get_database),
):
    _: blogs.Blog = await utils.delete_comment_handler(blog_id, comment_id, conn)
    response_object: dict = {"message": "Comment deleted successfully."}
    return response_object
