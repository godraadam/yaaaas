from sqlalchemy import Column, Integer, String
from app.model.base import Base

class User(Base):
    username = Column(String, unique=True, nullable=False)
    address = Column(String, unique=True, nullable=False)
    join_date = Column(Integer, nullable=False) # unix timestamp