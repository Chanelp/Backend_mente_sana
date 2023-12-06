from jwt import decode
from jwt.exceptions import PyJWKError
from dotenv import dotenv_values

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

OauthScheme = OAuth2PasswordBearer(tokenUrl="token")

secret = dotenv_values('vars.env')['encrypt_pass']

def verify_JSON_web_token(token: str = Depends(OauthScheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, secret, algorithms=["HS256"])
        userInfo: dict = payload
        if payload is None:
            raise credentials_exception
    except PyJWKError:
        raise credentials_exception
    return payload