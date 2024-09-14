from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class RepresentAcademicUnit(LinkModel):
    user_id: UUID
    academic_unit_id: UUID
    

