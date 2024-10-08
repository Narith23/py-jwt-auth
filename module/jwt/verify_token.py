from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError
from typing import Annotated

from helper.config import APP_ROUTE_PREFIX, JWT_ALGORITHM, JWT_SECRET_KEY


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/{APP_ROUTE_PREFIX}/auth/login/swagger")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except JWTError:  # You can catch specific JWT errors here
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
