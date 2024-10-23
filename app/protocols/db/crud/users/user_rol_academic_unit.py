from uuid import UUID
from sqlalchemy.orm import Session
from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user_rol_academic_unit import UserRolAcademicUnit
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate

class CRUDUserRolAcademicUnitProtocol(CRUDProtocol[UserRolAcademicUnit, UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate]):
    def get_by_user_id(self, *, user_id: UUID, db: Session) -> UserRolAcademicUnit:
        pass
    
    def get_student_committee(self, *, user_id:UUID, db: Session) -> UUID:
        pass