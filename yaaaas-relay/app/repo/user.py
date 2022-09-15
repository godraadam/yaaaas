from typing import Optional

from sqlalchemy.orm import Session

from app.model import User
from app.repo.base import CRUDBase
from app.schema.user import UserCreate, UserUpdate


class UserRepo(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_address(self, db: Session, address: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.address == address).first()


user_repo = UserRepo(User)
