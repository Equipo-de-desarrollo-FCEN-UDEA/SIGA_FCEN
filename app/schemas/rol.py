from pydantic import BaseModel
from typing import Optional

from app.schemas.model import GeneralResponse

class RolBase(BaseModel):
    name:str
    description: str
    
class RolCreate(RolBase):
    ...
    
class RolUpdate(BaseModel):
    ...
    
class RolInDB(GeneralResponse, RolBase):
    ...
    