from app.protocols.db.utils.link_model import LinkModel

from enum import Enum
from uuid import UUID

class VoteType(Enum):
    POSITIVE = "POSITIVO"
    NEGATIVE = "NEGATIVO"
    ABSTENTION = "ABSTENCION"
    CONSENSUS = "CONSENSO"

class Vote(LinkModel):
    voting_id: UUID
    user_id: UUID
    vote: VoteType