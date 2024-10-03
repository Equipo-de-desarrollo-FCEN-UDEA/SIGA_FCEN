from uuid import UUID
from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class RolBase(BaseModel):
    name:str
    scope: str
    description: str
    academic_unit_id: UUID
    
class RolCreate(RolBase):
    ...
    
class RolUpdate(BaseModel):
    ...
    
class RolInDB(GeneralResponse, RolBase):
    ...

class Rol(BaseModel):
    name: str
    description: str
    
    class Config:
        orm_mode = True
        from_attributes = True
    