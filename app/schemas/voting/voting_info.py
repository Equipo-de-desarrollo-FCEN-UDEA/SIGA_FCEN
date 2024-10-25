from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.protocols.db.models.voting.voting_info import VotingResult

class VotingStatus(BaseModel):
    result: VotingResult
    date: datetime
    observation: str | None

class VotingInfoBase(BaseModel):
    id_postgres: UUID | None = None
    statues: list[VotingStatus] | None = []

class VotingInfoCreate(VotingInfoBase):
    pass

class VotingInfoUpdate(BaseModel):
    pass

class VotingInfo(VotingInfoBase):
    pass
