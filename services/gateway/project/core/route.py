import functools
import re

import aiohttp
from fastapi import HTTPException, Request, Response, status

from project.core import config, jwt, requests
from project.utils import recaptcha


def route(
    request_method,
    path: str,
    status_code: int,
    service_config: str,
    payload_key: str | None = None,
    recaptcha_validation: bool = False,
    jwt_validation: bool = False,
    route_default: bool = True,
    original_prefix: str = "",
    new_prefix: str = "",
):
    app_any = request_method(path, status_code=status_code)

    def wrapper(f):
        @app_any
        @functools.wraps(f)
        async def inner(request: Request, response: Response, **kwargs):
            headers = {"Content-Type": "application/json"}
            scope = request.scope
            method = scope["method"].lower()
            path = scope["path"]
            query_string = scope.get("query_string")
            if jwt_validation:
                await jwt.validate_jwt_token(
                    request.headers.get("authorization"),
                    config.get_settings().secret,
                )
            if not route_default:
                path = re.sub(original_prefix, new_prefix, path)

            if recaptcha_validation:
                await recaptcha.validate_recaptcha(
                    request.headers.get("X-Recaptcha-Key")
                )

            service_url = getattr(config.get_settings(), service_config)

            url = f"{service_url}{path}"
            if query_string:
                url += f"?{query_string.decode('utf-8')}"
            payload_obj = kwargs.get(payload_key)
            payload = payload_obj.dict() if payload_obj else {}

            try:
                resp_data, status_code_from_service = await requests.make_request(
                    url=url, method=method, data=payload, headers=headers
                )
            except aiohttp.ClientConnectionError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Service is unavailable.",
                )
            except aiohttp.ContentTypeError:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Service error.",
                )

            response.status_code = status_code_from_service
            return resp_data

    return wrapper
