from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.academic_unit import AcademicUnit
from app.schemas.organization.academic_unit import AcademicUnitCreate, AcademicUnitUpdate


class AcademicUnitCrud(CRUDBase[AcademicUnit, AcademicUnitCreate, AcademicUnitUpdate]):
    ...


academic_unit_crud = AcademicUnitCrud(AcademicUnit)