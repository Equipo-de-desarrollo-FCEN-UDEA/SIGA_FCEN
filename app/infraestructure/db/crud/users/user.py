from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.user import User
from app.schemas.users.user import UserCreate, UserUpdate
from sqlalchemy.exc import NoResultFound
from app.core.exceptions import ORMError

from sqlalchemy.orm import Session, joinedload
from uuid import UUID


class UserCrud(CRUDBase[User, UserCreate, UserUpdate]):

    def get(self, *, id: UUID, db: Session) -> User:
        with db:
            return db.query(self.model).get(id)
        
    def get_by_email(self, *, email: str, db: Session) -> User:
        with db:
            try:
                response = db.query(User).filter(User.email == email).first()
                print(response.name)
                return response
            except NoResultFound as e:
                raise ORMError(str(e))


user_crud = UserCrud(User)