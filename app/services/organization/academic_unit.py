
from app.services.base import ServiceBase
from app.schemas.organization.academic_unit import AcademicUnitCreate, AcademicUnitUpdate
from app.protocols.db.models.organization.academic_unit import AcademicUnit
from app.protocols.db.crud.organization.academic_unit import CRUDAcademicUnitProtocol

class AcademicUnitService(ServiceBase[AcademicUnit, AcademicUnitCreate, AcademicUnitUpdate, CRUDAcademicUnitProtocol]):
    ...

academic_unit_svc = AcademicUnitService()