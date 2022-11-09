import asyncio

from fastapi import HTTPException, status

from project.core import config, requests


async def validate_recaptcha(key: str):
    url: str = (
        "https://www.google.com/recaptcha/api/siteverify?"
        f"secret={config.get_settings().recaptcha_secret}&"
        f"response={key}"
    )
    data, _ = await requests.make_request(
        url=url, method="post", headers={"Content-Type": "applications/json"}
    )
    if "score" in data and data.get("score") >= 0.7:
        return True
    else:
        await asyncio.sleep(8)
        raise HTTPException(
            status_code=status.HTTP_408_REQUEST_TIMEOUT,
            detail="Invalid activity detected.",
        )
