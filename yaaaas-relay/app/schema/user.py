from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    address: str

class UserCreate():
    username: str
    address: str
    join_date: int

class UserUpdate():
    address: str