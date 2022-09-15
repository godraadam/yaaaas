from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    address: str


class UserCreate(UserBase):
    join_date: int


class UserUpdate:
    address: str


class UserInDB(UserBase):
    id: str
