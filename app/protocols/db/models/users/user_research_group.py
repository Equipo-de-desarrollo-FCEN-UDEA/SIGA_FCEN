from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class UserResearchGroup(LinkModel):
    user_id: UUID
    research_group_id: UUID