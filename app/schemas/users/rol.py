from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class RolBase(BaseModel):
    name:str
    scope: int
    description: str
    
class RolCreate(RolBase):
    ...
    
class RolUpdate(BaseModel):
    name:str | None
    scope: int | None
    description: str | None
    
class RolInDB(GeneralResponse, RolBase):
    ...
    