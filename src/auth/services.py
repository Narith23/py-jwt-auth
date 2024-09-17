# This is a sample services.py file
import logging

from helper.best_response import internal_server_error_response, success_response
from module.jwt.generate_token import create_access_token, create_refresh_token


class AuthService:
    @staticmethod
    async def login(request: dict, swagger: bool = False):
        try:
            data = dict(
                username=request.get("username"),
                password=request.get("password"),
            )
            if swagger:
                return dict(
                    access_token=await create_access_token(data),
                    refresh_token=await create_refresh_token(data),
                )
            return success_response(
                result=dict(
                    access_token=await create_access_token(data),
                    refresh_token=await create_refresh_token(data),
                )
            )
        except Exception as e:
            logging.exception(e)
            return internal_server_error_response()
