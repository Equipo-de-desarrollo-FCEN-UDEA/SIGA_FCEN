from app.protocols.db.utils.base_model import BaseModel

from uuid import UUID

class Voting(BaseModel):
    academic_unit_id: UUID
    user_application_id: UUID