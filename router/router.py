from fastapi import APIRouter

from helper.config import APP_ROUTE_PREFIX
from src.auth.router import router as auth_router
from src.user.router import router as user_router

router = APIRouter()

# Authorization Router
router.include_router(auth_router, prefix=f"/{APP_ROUTE_PREFIX}/auth", tags=["Authorization".upper()])

# User Router
router.include_router(user_router, prefix=f"/{APP_ROUTE_PREFIX}/user", tags=["User".upper()])
