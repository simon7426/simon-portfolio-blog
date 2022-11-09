from urllib.request import Request

from fastapi import status
from fastapi.responses import JSONResponse


class DBNotInitializedError(Exception):
    def __init__(self) -> None:
        pass


async def db_not_initialized_exception_handler(_: Request):
    raise DBNotInitializedError


async def value_error_exception_handler(request: Request, exc: ValueError):
    print(exc)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detatil": "Value Error"},
    )
