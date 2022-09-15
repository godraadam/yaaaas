from fastapi import FastAPI
from app.api.index import index_router
from app.config.index import settings

app = FastAPI(title=f"{settings.SERVICE_NAME} docs")
app.include_router(index_router)


@app.on_event("startup")
def on_startup():
    pass


@app.on_event("shutdown")
def on_shutdown():
    pass


@app.get("/")
def root():
    return f"{settings.SERVICE_NAME}` is running. See /docs for more info."
