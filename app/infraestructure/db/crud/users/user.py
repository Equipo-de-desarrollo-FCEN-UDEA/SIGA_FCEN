from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.user import User
from app.infraestructure.db.models.user.user_rol_academic_unit import UserRolAcademicUnit
from app.schemas.users.user import UserCreate, UserUpdate
from sqlalchemy.exc import NoResultFound
from app.core.exceptions import ORMError

from sqlalchemy.orm import Session, contains_eager
from uuid import UUID


class UserCrud(CRUDBase[User, UserCreate, UserUpdate]):

    def get(self, *, id: UUID, db: Session) -> User:
        with db:
            return db.query(self.model).get(id)
        
    def get_by_email(self, *, email: str, db: Session) -> User:
        with db:
            response = db.query(User).filter((User.email == email) & (UserRolAcademicUnit.is_active == True)).first()
            if not response:
                raise ORMError(f"No user found with email {email}")

            response.user_roles_academic_units = [
                role for role in response.user_roles_academic_units if role.is_active
            ]

            return response

user_crud = UserCrud(User)