from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from project.core import exceptions
from project.router import router

origins = [
    "http://localhost:3000",
    "https://blog.simonislam.com",
    "https://blog-admin.simonislam.com",
    "http://hello.world",
    "http://admin.hello.world",
]


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(HTTPException, exceptions.http_error_handler)
    app.add_exception_handler(
        HTTP_422_UNPROCESSABLE_ENTITY, exceptions.http_422_error_handler
    )

    # * Adding Routers to app *#
    app.include_router(router)

    return app


app = create_app()
