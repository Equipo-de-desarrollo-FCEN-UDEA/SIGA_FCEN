from app.protocols.db.utils.link_model import LinkModel

from uuid import UUID

class UserApplicationAcademicUnit(LinkModel):
    user_application_id: UUID
    academic_unit_id: UUID