from jwt import decode
from jwt.exceptions import PyJWKError, DecodeError
from fastapi import Depends, HTTPException, status, Request

from utils.env import read_env_key

SECRET = read_env_key('encrypt_pass')

def verify_JSON_web_token(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token = request.headers.get('authentication-token')

        if token is None: 
            raise credentials_exception

        payload = decode(token, SECRET, algorithms=["HS256"])

        if payload is None:
            raise credentials_exception
    except PyJWKError:
        raise credentials_exception
    except DecodeError:
        raise credentials_exception
    else:
        return payload