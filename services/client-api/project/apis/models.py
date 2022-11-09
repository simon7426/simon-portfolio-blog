from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, validator


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CommentPost(BaseModel):
    email: EmailStr
    display_name: str
    body: str

    class Config:
        schema_extra = {
            "example": {
                "email": "abc@example.com",
                "display_name": "test-name",
                "body": "Test Comment for Test Blog.",
            }
        }


class Comment(CommentPost):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_on: datetime

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Test Title",
                "body": "Test Body for Test Blog.",
                "tags": ["tag1", "tag2"],
            }
        }


class Blog(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    body: str
    tags: List[str]
    comments: List[Comment] = None
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Test Title",
                "body": "Test Body for Test Blog.",
                "tags": ["tag1", "tag2"],
                "comments": ["sample comment 1", "sample comment 2"],
                "created_on": "2022-01-01",
            }
        }


class BlogCollection(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    tags: List[str]
    body: str = Field(exclude=True)
    summary: str = None
    created_at: datetime
    updated_at: datetime | None = None

    @validator("summary", pre=True, always=True)
    def make_summary(cls, _: str, values: dict):
        return f"{values['body'][:250]}"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Test Title",
                "summary": "Test Body summary",
                "tags": ["tag1", "tag2"],
            }
        }
