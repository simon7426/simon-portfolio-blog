from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from project.apis.blog import crud
from project.apis.models import Blog, BlogCollection, CommentPost, PyObjectId
from project.utils.db import get_db

router = APIRouter(prefix="/api/v1/blogs")


@router.get("", response_model=List[BlogCollection])
async def get_blogs(tag: str = "", db=Depends(get_db)):
    response: List[BlogCollection] = await crud.get_all_blogs(tag, db)
    return response


@router.get("/{id}", response_model=Blog)
async def get_single_blog(id: PyObjectId, db=Depends(get_db)):
    response = await crud.get_blog(id, db)
    print(response)
    if response is None:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    return response


@router.post("/{id}/comment", response_model=Blog)
async def add_comment(id: PyObjectId, data: CommentPost, db=Depends(get_db)):
    post_data = jsonable_encoder(data)
    _ = await crud.add_comment(id, post_data, db)
    blog = await crud.get_blog(id, db)
    return blog
