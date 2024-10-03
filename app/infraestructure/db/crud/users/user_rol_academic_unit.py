from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.user.user_rol_academic_unit import UserRolAcademicUnit
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate

class UserRolAcademicUnitCrud(CRUDBase[UserRolAcademicUnit, UserRolAcademicUnitCreate, UserRolAcademicUnitUpdate]):
    ...
    
user_rol_academic_unit_crud = UserRolAcademicUnitCrud(UserRolAcademicUnit)