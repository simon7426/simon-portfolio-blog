from fastapi.openapi.utils import get_openapi
from yaml import safe_dump

from project import app


def generate_schema():
    with open("./docs/api/openapi.yaml", "w") as f:
        f.write(
            safe_dump(
                get_openapi(
                    title=app.title,
                    version=app.version,
                    openapi_version=app.openapi_version,
                    description=app.description,
                    routes=app.routes,
                )
            )
        )
