from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.user import User
from app.schemas.users.user import UserCreate, UserUpdate

from sqlalchemy.orm import Session, joinedload
from uuid import UUID


class UserCrud(CRUDBase[User, UserCreate, UserUpdate]):

    def get(self, *, id: UUID, db: Session) -> User:
        with db:
            return db.query(self.model).get(id)


user_crud = UserCrud(User)