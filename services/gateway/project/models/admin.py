from typing import List

from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {"username": "test-username", "password": "test-password"}
        }


class BlogIn(BaseModel):
    title: str
    body: str
    tags: List[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Test Title",
                "body": "Test Body",
                "tags": ["tag1", "tag2"],
            }
        }
