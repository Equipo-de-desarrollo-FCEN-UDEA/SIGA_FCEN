from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class ResearchGroup(BaseModel):
    name: str
    description: str
    email: str
    academic_unit_id: UUID