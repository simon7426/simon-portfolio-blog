from datetime import datetime
from typing import Any, List

from bson import ObjectId
from pydantic import BaseModel, Field


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


class Blog(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    body: str
    tags: List[str]
    comments: List[Any] = None
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
                "created_at": "2022-01-01",
                "updated_at": "2022-01-01",
            }
        }
