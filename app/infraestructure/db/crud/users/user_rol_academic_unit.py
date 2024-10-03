from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.user_rol_academic_unit import UserRolAcademicUnit
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate


class UserRolAcademicUnitCrud(CRUDBase[UserRolAcademicUnit, UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate]):
    def get_by_user_id(self, *, user_id: UUID, db: Session) -> UserRolAcademicUnit:
        return db.query(UserRolAcademicUnit).options(
            joinedload(UserRolAcademicUnit.rol),
            joinedload(UserRolAcademicUnit.academic_unit)
        ).filter(self.model.user_id == user_id).all()
    
user_rol_academic_unit_crud = UserRolAcademicUnitCrud(UserRolAcademicUnit)