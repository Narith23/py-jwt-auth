from typing import Optional, List, Generic, TypeVar, Union

from fastapi import status
from pydantic import BaseModel

T = TypeVar("T")


# Make a best response for a given status code
class ResponseModel(BaseModel, Generic[T]):
    status_code: Optional[int] = status.HTTP_200_OK
    success: Optional[bool] = True
    message: Optional[str] = "OK"
    result: Union[T, List[T], None]


class ListResponseModel(BaseModel, Generic[T]):
    status_code: Optional[int] = status.HTTP_200_OK
    success: Optional[bool] = True
    message: Optional[str] = "OK"
    result: Union[List[T], None]


# status_code: 200
def success_response(
    status_code: int = status.HTTP_200_OK,
    message: Optional[str] = "OK",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result
        )
    else:
        return ResponseModel(status_code=status_code, message=message, result=result)


# status_code: 201
def created_response(
    status_code: int = status.HTTP_201_CREATED,
    message: Optional[str] = "Created",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result
        )
    else:
        return ResponseModel(status_code=status_code, message=message, result=result)


# status_code: 204
def no_content_response(
    status_code: int = status.HTTP_204_NO_CONTENT,
    message: Optional[str] = "No Content",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result
        )
    else:
        return ResponseModel(status_code=status_code, message=message, result=result)


# status_code: 400
def bad_request_response(
    status_code: int = status.HTTP_400_BAD_REQUEST,
    message: Optional[str] = "Bad Request",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
    else:
        return ResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )


# status_code: 404
def not_found_response(
    status_code: int = status.HTTP_404_NOT_FOUND,
    message: Optional[str] = "Not Found",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
    else:
        return ResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )


# status_code: 500
def internal_server_error_response(
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    message: Optional[str] = "Internal Server Error",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
    else:
        return ResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )


# status_code: 401
def unauthorized_response(
    status_code: int = status.HTTP_401_UNAUTHORIZED,
    message: Optional[str] = "Unauthorized",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
    else:
        return ResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )


# status_code: 403
def forbidden_response(
    status_code: int = status.HTTP_403_FORBIDDEN,
    message: Optional[str] = "Forbidden",
    result: Optional[T | List[T]] = None,
) -> dict:
    if isinstance(result, list):
        return ListResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
    else:
        return ResponseModel(
            status_code=status_code, message=message, result=result, success=False
        )
