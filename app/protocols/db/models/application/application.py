from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class Application(BaseModel):
    name: str
    description: str
    academic_unit_id: UUID

