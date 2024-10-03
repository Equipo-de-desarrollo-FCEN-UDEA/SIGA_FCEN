from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user_rol_academic_unit import UserRolAcademicUnit
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate

class CRUDUserRolAcademicUnitProtocol(CRUDProtocol[UserRolAcademicUnit, UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate]):
    ...