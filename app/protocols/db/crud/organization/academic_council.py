from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.academic_council import AcademicCouncil
from app.schemas.organization.academic_council import AcademicCouncilCreate, AcademicCouncilUpdate

class CRUDAcademicCouncilProtocol(CRUDProtocol[AcademicCouncil, AcademicCouncilCreate, AcademicCouncilUpdate]):
    pass