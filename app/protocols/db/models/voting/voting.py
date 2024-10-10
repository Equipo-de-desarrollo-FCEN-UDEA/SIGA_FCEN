from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
from uuid import UUID

class VotingStatus(Enum):
    OPEN = "Abierto"
    APPROVED = "Aprobada"
    DECLINED = "Rechazada"

class Voting(BaseModel):
    academic_unit_id: UUID
    application_id: UUID
    status: VotingStatus