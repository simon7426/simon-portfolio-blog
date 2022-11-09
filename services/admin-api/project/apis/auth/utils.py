from datetime import datetime

from fastapi import status
from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from project.apis.auth import crud
from project.core import exceptions, jwt, security
from project.models import users


async def create_user(
    conn: AsyncIOMotorClient, username: str, email: str, password: str
) -> users.User:
    user: users.User | None = await crud.get_user_by_username(username, conn)
    if user:
        raise exceptions.UserAlreadyExistsError
    salt: str = security.generate_salt(16)
    data = {
        "username": username,
        "email": email,
        "salt": salt,
        "password": security.hash_password(password + salt),
        "created_on": datetime.utcnow(),
    }
    response = await crud.add_user(data, conn)
    return await crud.get_user(str(response.inserted_id), conn)


async def login_handler(
    username: str, password: str, conn: AsyncIOMotorClient
) -> users.Token:
    user: users.User | None = await crud.get_user_by_username(username, conn)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Username/Password."
        )
    if user and security.verify_password(user.password, password + user.salt):
        token: users.Token = await jwt.create_access_token(user.username)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Username/Password."
        )
    return users.Token(access_token=token)
