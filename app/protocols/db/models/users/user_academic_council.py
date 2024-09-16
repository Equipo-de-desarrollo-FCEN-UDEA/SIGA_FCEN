from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class UserAcademicCouncil(LinkModel):
    user_id: UUID
    academic_council_id: UUID