from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.academic_unit import AcademicUnit
from app.schemas.organization.academic_unit import AcademicUnitCreate, AcademicUnitUpdate

class CRUDAcademicUnitProtocol(CRUDProtocol[AcademicUnit, AcademicUnitCreate, AcademicUnitUpdate]):
    ...