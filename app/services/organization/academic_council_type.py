from app.services.base import ServiceBase
from app.schemas.organization.academic_council_type import AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate
from app.protocols.db.models.organization.academic_council_type import AcademicCouncilType
from app.protocols.db.crud.organization.academic_council_type import CRUDAcademicCouncilTypeProtocol

class AcademicCouncilTypeService(ServiceBase[AcademicCouncilType, AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate, CRUDAcademicCouncilTypeProtocol]):
    pass

academic_council_type_svc = AcademicCouncilTypeService()