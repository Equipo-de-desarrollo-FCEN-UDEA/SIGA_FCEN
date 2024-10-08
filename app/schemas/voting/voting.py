from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse
from app.protocols.db.models.voting.voting import VotingStatus

class VotingBase(BaseModel):
    academic_unit_id: UUID
    application_id: UUID
    status: VotingStatus

class VotingCreate(VotingBase):
    pass

class VotingUpdate(BaseModel):
    academic_unit_id: UUID | None
    application_id: UUID | None
    status: VotingStatus | None