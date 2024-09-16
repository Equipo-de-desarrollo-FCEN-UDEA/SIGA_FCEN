from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.academic_unit_type import AcademicUnitType
from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeUpdate


class AcademicUnitTypeCrud(CRUDBase[AcademicUnitType, AcademicUnitTypeCreate, AcademicUnitTypeUpdate]):
    ...


academic_unit_type_crud = AcademicUnitTypeCrud(AcademicUnitType)