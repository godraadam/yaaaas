from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_db
from app.schema.user import UserCreate
from app.schema.auth import LoginPayload, SignupPayload
from app.service.auth import auth_service
from app.service.user import user_service
from starlette import status
from sqlalchemy.orm import Session
import util

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/signup")
def signup(signup_payload: SignupPayload, db: Session = Depends(get_db)):
    # validate signature and pow token
    validated = auth_service.validate_signup_payload(signup_payload)
    if not validated:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    # check that user can be registered
    if not user_service.can_create_user(db=db, username=signup_payload.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already taken."
        )

    # create user
    address = util.hashing.derive_address_from_pubkey(signup_payload.pubkey)
    create_payload = UserCreate(username=signup_payload.username, address=address)
    return user_service.create_user(db=db, payload=create_payload)


@auth_router.post("/login")
def login(login_payload: LoginPayload):
    raise NotImplementedError()
