from app.services.base import ServiceBase
from app.schemas.users.user_academic_council import UserAcademicCouncilCreate, UserAcademicCouncilUpdate
from app.protocols.db.models.users.user_academic_council import UserAcademicCouncil
from app.protocols.db.crud.users.user_academic_council import CRUDUserAcademicCouncilProtocol

class UserAcademicCouncilService(ServiceBase[UserAcademicCouncil, UserAcademicCouncilCreate, UserAcademicCouncilUpdate, CRUDUserAcademicCouncilProtocol]):
    ...


user_academic_council_svc = UserAcademicCouncilService()