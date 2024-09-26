from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class UserRol(LinkModel):
    user_id: UUID
    rol_id: UUID