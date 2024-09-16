from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.academic_unit_type import AcademicUnitType
from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeUpdate

class CRUDAcademicUnitTypeProtocol(CRUDProtocol[AcademicUnitType, AcademicUnitTypeCreate, AcademicUnitTypeUpdate]):
    ...