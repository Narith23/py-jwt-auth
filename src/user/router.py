# This is a sample router.py file
from fastapi import APIRouter, Depends, status

from helper.best_response import success_response
from module.jwt.verify_token import get_current_user
from src.user.model import CurrentUser


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: CurrentUser = Depends(get_current_user)):
    return success_response(result=user)
