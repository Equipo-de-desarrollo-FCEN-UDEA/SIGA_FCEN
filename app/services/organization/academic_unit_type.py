from app.services.base import ServiceBase
from app.schemas.organization.academic_unit_type import AcademicUnitTypeCreate, AcademicUnitTypeUpdate
from app.protocols.db.models.organization.academic_unit_type import AcademicUnitType
from app.protocols.db.crud.organization.academic_unit_type import CRUDAcademicUnitTypeProtocol

class AcademicUnitTypeService(ServiceBase[AcademicUnitType, AcademicUnitTypeCreate, AcademicUnitTypeUpdate, CRUDAcademicUnitTypeProtocol]):
    ...

academic_unit_type_svc = AcademicUnitTypeService()