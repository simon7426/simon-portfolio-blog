from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: bytes
    salt: str

    class Config:
        schema_extra = {
            "example": {
                "username": "test-username",
                "email": "test-email@example.com",
                "password": "test-password-hash",
                "salt": "test-salt",
            }
        }


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {"username": "test-username", "password": "test-password"}
        }


class Token(BaseModel):
    access_token: str

    class Config:
        schema_extra = {"example": {"access_token": "test-access-token"}}
