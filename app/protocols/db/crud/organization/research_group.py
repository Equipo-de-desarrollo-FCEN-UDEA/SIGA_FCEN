from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.organization.research_group import ResearchGroup
from app.schemas.organization.research_group import ResearchGroupCreate, ResearchGroupUpdate

class CRUDResearchGroupProtocol(CRUDProtocol[ResearchGroup, ResearchGroupCreate, ResearchGroupUpdate]):
    pass