from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class RolBase(BaseModel):
    name:str
    description: str
    
class RolCreate(RolBase):
    ...
    
class RolUpdate(BaseModel):
    ...
    
class RolInDB(GeneralResponse, RolBase):
    ...
    