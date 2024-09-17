from app.services.base import ServiceBase
from app.schemas.users.user_research_group import UserResearchGroupCreate, UserResearchGroupUpdate
from app.protocols.db.models.users.user_research_group import UserResearchGroup
from app.protocols.db.crud.users.user_research_group import CRUDUserResearchGroupProtocol

class UserResearchGroupService(ServiceBase[UserResearchGroup, UserResearchGroupCreate, UserResearchGroupUpdate, CRUDUserResearchGroupProtocol]):
    ...


user_research_group_svc = UserResearchGroupService()