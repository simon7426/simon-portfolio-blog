import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.apis import alive
from project.apis.blog import views as blogs
from project.utils import db, exceptions

log = logging.getLogger("uvicorn")

origins = [
    "https://blog.simonislam.com",
    "http://localhost:3000",
    "http://hello.world",
    "http://admin.hello.world",
    "https://blog-admin.simonislam.com",
]


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # * Adding Routers to app *#
    app.include_router(alive.router)
    app.include_router(blogs.router)

    # * Adding Exception Handlers *#
    app.add_exception_handler(
        exceptions.DBNotInitializedError,
        exceptions.db_not_initialized_exception_handler,
    )
    app.add_exception_handler(
        ValueError,
        exceptions.value_error_exception_handler,
    )

    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    db.init_db()
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
