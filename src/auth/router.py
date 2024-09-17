# This is a sample router.py file
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.services import AuthService

router = APIRouter()


@router.post("/login/swagger", status_code=status.HTTP_200_OK)
async def login_swagger(
    request: OAuth2PasswordRequestForm = Depends(),
):
    return await AuthService.login(
        request=dict(username=request.username, password=request.password), swagger=True
    )


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    request: OAuth2PasswordRequestForm = Depends(),
):
    return await AuthService.login(
        request=dict(username=request.username, password=request.password)
    )
