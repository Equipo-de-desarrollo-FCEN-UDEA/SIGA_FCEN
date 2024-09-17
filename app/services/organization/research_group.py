from app.services.base import ServiceBase
from app.schemas.organization.research_group import ResearchGroupCreate, ResearchGroupUpdate
from app.protocols.db.models.organization.research_group import ResearchGroup
from app.protocols.db.crud.organization.research_group import CRUDResearchGroupProtocol

class ResearchGroupService(ServiceBase[ResearchGroup, ResearchGroupCreate, ResearchGroupUpdate, CRUDResearchGroupProtocol]):
    pass

research_group_svc = ResearchGroupService()