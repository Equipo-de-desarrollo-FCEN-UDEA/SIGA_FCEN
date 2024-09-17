from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user_academic_council import UserAcademicCouncil
from app.schemas.users.user_academic_council import UserAcademicCouncilCreate, UserAcademicCouncilUpdate

class CRUDUserAcademicCouncilProtocol(CRUDProtocol[UserAcademicCouncil, UserAcademicCouncilCreate, UserAcademicCouncilUpdate]):
    ...