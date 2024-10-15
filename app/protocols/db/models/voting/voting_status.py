from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
from uuid import UUID


class VotingStatusType(Enum):
    OPEN = "Abierto"
    APPROVED = "Aprobada"
    DECLINED = "Rechazada"

class VotingStatus(BaseModel):
    name: VotingStatusType
    