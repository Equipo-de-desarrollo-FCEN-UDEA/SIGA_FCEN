from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class ResearchGroup(BaseModel):
    name: str
    description: str | None
    email: str | None
    academic_unit_id: UUID