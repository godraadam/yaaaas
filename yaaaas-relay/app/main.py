from fastapi import FastAPI
from app.api.index import index_router

app = FastAPI(title="YAAAAS relay server")
app.include_router(index_router)


@app.on_event("startup")
def on_startup():
    pass


@app.on_event("shutdown")
def on_shutdown():
    pass
