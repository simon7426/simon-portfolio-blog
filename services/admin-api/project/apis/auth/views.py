from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from project.apis.auth import utils
from project.db import mongodb
from project.models import users

router = APIRouter(prefix="/api/v1/admin/auth")


@router.post("/login", response_model=users.Token)
async def login(
    data: users.UserLogin,
    conn=Depends(mongodb.get_database),
):
    post_data = jsonable_encoder(data)
    token: users.Token = await utils.login_handler(
        username=post_data["username"],
        password=post_data["password"],
        conn=conn,
    )
    return token
