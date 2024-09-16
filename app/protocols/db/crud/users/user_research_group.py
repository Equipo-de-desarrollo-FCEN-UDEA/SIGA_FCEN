from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.user_research_group import UserResearchGroup
from app.schemas.users.user_research_group import UserResearchGroupCreate, UserResearchGroupUpdate

class CRUDUserResearchGroupProtocol(CRUDProtocol[UserResearchGroup, UserResearchGroupCreate, UserResearchGroupUpdate]):
    ...
