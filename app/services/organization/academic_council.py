from app.services.base import ServiceBase
from app.schemas.organization.academic_council import AcademicCouncilCreate, AcademicCouncilUpdate
from app.protocols.db.models.organization.academic_council import AcademicCouncil
from app.protocols.db.crud.organization.academic_council import CRUDAcademicCouncilProtocol

class AcademicCouncilService(ServiceBase[AcademicCouncil, AcademicCouncilCreate, AcademicCouncilUpdate, CRUDAcademicCouncilProtocol]):
    pass

academic_council_svc = AcademicCouncilService()