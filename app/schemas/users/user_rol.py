from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class UserRolBase(BaseModel):
    rol_id: UUID
    user_id: UUID
    is_active: bool| None = True
    
    
class UserRolCreate(UserRolBase):
    ...
    
class UserRolUpdate(BaseModel):
    ...
    
class UserRolInDB(GeneralResponse, UserRolBase):
    ...

class UserRol(UserRolBase):
    id: UUID
    
    class Config:
        orm_mode = True