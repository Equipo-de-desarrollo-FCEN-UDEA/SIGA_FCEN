from pydantic import BaseModel
from uuid import UUID
from app.protocols.db.models.voting.voting_status import VotingStatusType
from app.schemas.utils.base_model import GeneralResponse

class VotingStatusBase(BaseModel):
    voting_id: UUID
    status: VotingStatusType


class VotingStatusCreate(VotingStatusBase):
    pass

class VotingStatusUpdate(BaseModel):
    voting_id: UUID | None = None
    status: VotingStatusType | None = None