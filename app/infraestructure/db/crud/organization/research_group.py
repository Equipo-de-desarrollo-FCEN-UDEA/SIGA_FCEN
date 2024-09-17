from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.research_group import ResearchGroup
from app.schemas.organization.research_group import ResearchGroupCreate, ResearchGroupUpdate

class ResearchGroupCrud(CRUDBase[ResearchGroup, ResearchGroupCreate, ResearchGroupUpdate]):
    pass

research_group_crud = ResearchGroupCrud(ResearchGroup)