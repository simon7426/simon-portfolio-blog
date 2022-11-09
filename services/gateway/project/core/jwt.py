import jwt
from fastapi import status
from fastapi.exceptions import HTTPException


async def validate_jwt_token(token: str, secret: str):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )
    try:
        payload = jwt.decode(token.split(" ")[-1], key=secret, algorithms=["HS256"])
        if payload["type"] != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired Token"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        )
