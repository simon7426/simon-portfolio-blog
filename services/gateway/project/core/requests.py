import aiohttp
import async_timeout

from project.core import config


async def make_request(url: str, method: str, data: dict = None, headers: dict = None):
    if not data:
        data = {}
    with async_timeout.timeout(config.get_settings().gateway_timeout):
        async with aiohttp.ClientSession() as session:
            request = getattr(session, method)
            async with request(url, json=data, headers=headers) as response:
                data = await response.json()
                return (data, response.status)
