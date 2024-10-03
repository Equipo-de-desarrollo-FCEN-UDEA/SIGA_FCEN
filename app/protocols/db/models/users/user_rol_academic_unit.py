from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class UserRolAcademicUnit(LinkModel):
    user_id: UUID
    rol_id: UUID
    academic_unit_id: UUID
    is_active: bool