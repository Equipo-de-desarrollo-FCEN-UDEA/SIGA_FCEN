from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class ProfessorTypeBase(BaseModel):
    name:str

class ProfessorTypeCreate(ProfessorTypeBase):
    ...

class ProfessorTypeUpdate(BaseModel):
    ...

class ProfessorTypeDB(GeneralResponse, ProfessorTypeBase):
    ...
