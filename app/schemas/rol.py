from pydantic import BaseModel
from typing import Optional

<<<<<<< HEAD:app/schemas/rol.py
from app.schemas.model import GeneralResponse
=======
from app.schemas.utils.base_model import GeneralResponse
>>>>>>> develop:app/schemas/users/rol.py

class RolBase(BaseModel):
    name:str
    description: str
    
class RolCreate(RolBase):
    ...
    
class RolUpdate(BaseModel):
    ...
    
class RolInDB(GeneralResponse, RolBase):
    ...
    