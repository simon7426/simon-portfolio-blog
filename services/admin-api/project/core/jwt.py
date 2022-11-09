from datetime import datetime, timedelta
from typing import Optional

import jwt

from project.core import config


async def create_access_token(
    username: str, expires_delta: Optional[timedelta] = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)

    data = {"sub": username, "exp": expire, "type": "access"}
    encoded_jwt = jwt.encode(
        data, key=str(config.get_settings().secret), algorithm="HS256"
    )
    return encoded_jwt
