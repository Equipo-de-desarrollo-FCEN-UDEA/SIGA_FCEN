from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class UserResearchGroupBase(BaseModel):
    user_id: UUID
    research_group_id: UUID
    
class UserResearchGroupCreate(UserResearchGroupBase):
    ...

class UserResearchGroupUpdate(BaseModel):
    ...

class UserResearchGroupDB(GeneralResponse, UserResearchGroupBase):
    ...
