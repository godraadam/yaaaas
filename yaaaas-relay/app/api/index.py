from fastapi import APIRouter
from app.api.auth import auth_router
from app.config.index import settings

index_router = APIRouter(prefix="/api")
index_router.include_router(auth_router)


@index_router.get("/")
def api_root():
    return f"{settings.SERVICE_NAME} api root. See /docs for more info."
