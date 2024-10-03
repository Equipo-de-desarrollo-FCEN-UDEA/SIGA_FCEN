from app.services.base import ServiceBase
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate, UserRolAcademicUnitInDB
from app.protocols.db.models.users.user_rol_academic_unit import UserRolAcademicUnit
from app.protocols.db.crud.users.user_rol_academic_unit import CRUDUserRolAcademicUnitProtocol

class UserRolAcademicUnitService(ServiceBase[UserRolAcademicUnit, UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate, CRUDUserRolAcademicUnitProtocol]):
    ...

user_rol_academic_unit_svc = UserRolAcademicUnitService()
