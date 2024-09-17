from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class UserAcademicCouncilBase(BaseModel):
    user_id: UUID
    academic_council_id: UUID
    
class UserAcademicCouncilCreate(UserAcademicCouncilBase):
    ...

class UserAcademicCouncilUpdate(BaseModel):
    ...

class UserAcademicCouncilDB(GeneralResponse, UserAcademicCouncilBase):
    ...

