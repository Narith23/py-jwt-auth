from typing import Union

from fastapi import FastAPI

from router.router import router as public_api

from helper.best_response import success_response
from helper.config import (
    APP_DESCRIPTION,
    APP_ENV,
    APP_HOST,
    APP_NAME,
    APP_ROUTE_PREFIX,
    APP_VERSION,
)

if APP_ENV == "development":
    swagger_url = f"/{APP_ROUTE_PREFIX}/docs"
else:
    swagger_url = None

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    docs_url=swagger_url,
    redoc_url=f"/{APP_ROUTE_PREFIX}/docs/redoc",
    openapi_url=f"/{APP_ROUTE_PREFIX}/docs/openapi.json",
)

app.include_router(public_api)

# add_pagination(app)


@app.get("/", tags=["default".upper()])
def read_root():
    return success_response(
        message=f"Welcome to {APP_NAME} {APP_VERSION} API",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=APP_HOST, port=8000)
