from click import pass_context
from fastapi import APIRouter
from app.schema.auth import LoginPayload, SignupPayload

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/signup")
def signup(signup_payload: SignupPayload):
    raise NotImplementedError()


@auth_router.post("/login")
def login(login_payload: LoginPayload):
    raise NotImplementedError()
