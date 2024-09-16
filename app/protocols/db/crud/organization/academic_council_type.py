from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.academic_council_type import AcademicCouncilType
from app.schemas.organization.academic_council_type import AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate

class CRUDAcademicCouncilTypeProtocol(CRUDProtocol[AcademicCouncilType, AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate]):
    pass