from fastapi import APIRouter
from app.api.auth import auth_router

index_router = APIRouter(prefix="/api")
index_router.include_router(auth_router)
