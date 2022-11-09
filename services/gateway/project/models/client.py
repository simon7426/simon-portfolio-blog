from pydantic import BaseModel, EmailStr


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
