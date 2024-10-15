from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
from uuid import UUID

class Voting(BaseModel):
    academic_unit_id: UUID
    application_id: UUID
    voting_status_id: UUID