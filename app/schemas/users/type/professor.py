from enum import IntEnum
from pydantic import BaseModel
from uuid import UUID


from app.schemas.utils.base_model import GeneralResponse



class ProfessorBase(BaseModel):
    id_postgres: UUID
    type: str

class ProfessorCreate(ProfessorBase):
    ... 

class ProfessorUpdate(BaseModel):
    ...

class ProfessorInDB(ProfessorBase):
    ...