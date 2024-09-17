from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

from uuid import UUID

class UserRolBase(BaseModel):
    rol_id: UUID
    user_id: UUID
    observation:str
    
    
class UserRolCreate(UserRolBase):
    ...
    
class UserRolUpdate(BaseModel):
    ...
    
class UserRolInDB(GeneralResponse, UserRolBase):
    ...