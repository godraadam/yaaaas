import time
from fastapi import HTTPException
from app.schema.user import UserCreate, UserUpdate, UserInDB, UserBase
from app.repo.user import user_repo
from starlette import status
from sqlalchemy.orm import Session


class UserService:
    def can_create_user(self, db: Session, username: str):
        # check if username is available
        user_from_repo: UserInDB = user_repo.get_by_username(db=db, username=username)
        if user_from_repo:
            return False

    def create_user(self, db: Session, payload: UserBase):

        # build create payload
        create_payload = UserCreate(**payload, join_date=time.time())

        # persist user object
        return user_repo.create(db=db, obj_in=create_payload)

    def update_user(self, update_payload: UserUpdate):
        raise NotImplementedError()


user_service = UserService()
