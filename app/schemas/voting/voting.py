from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class VotingBase(BaseModel):
    academic_unit_id: UUID
<<<<<<< Updated upstream
    application_id: UUID
    voting_status_id: UUID
=======
    user_application_id: UUID
>>>>>>> Stashed changes

class VotingCreate(VotingBase):
    pass

class VotingUpdate(BaseModel):
    academic_unit_id: UUID | None
<<<<<<< Updated upstream
    application_id: UUID | None
    voting_status_id: UUID | None
=======
    user_application_id: UUID | None
>>>>>>> Stashed changes
