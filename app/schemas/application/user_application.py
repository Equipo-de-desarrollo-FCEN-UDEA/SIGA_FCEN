from pydantic import BaseModel
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse

class UserApplicationBase(BaseModel):
    user_id: UUID
    application_id: UUID

class UserApplicationCreate(UserApplicationBase):
    pass 

class UserApplicationUpdate(BaseModel):
    user_id: UUID | None
    application_id: UUID | None
    application_status_id: UUID | None

class UserApplicationCreateInDB(GeneralResponse, UserApplicationBase):
    pass