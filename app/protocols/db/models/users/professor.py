from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class Professor(LinkModel):
    user_id: UUID
    academic_unit_id: UUID
    professor_type_id: UUID
    