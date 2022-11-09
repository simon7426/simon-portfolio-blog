from collections.abc import Iterable

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


class UserAlreadyExistsError(Exception):
    pass


async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)


async def http_422_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handler for 422 error to transform default pydantic error object to gothinkster format
    """

    errors = {"body": []}

    if isinstance(exc.detail, Iterable) and not isinstance(
        exc.detail, str
    ):  # check if error is pydantic's model error
        for error in exc.detail:
            error_name = ".".join(
                error["loc"][1:]
            )  # remove 'body' from path to invalid element
            errors["body"].append({error_name: error["msg"]})
    else:
        errors["body"].append(exc.detail)

    return JSONResponse({"errors": errors}, status_code=HTTP_422_UNPROCESSABLE_ENTITY)
