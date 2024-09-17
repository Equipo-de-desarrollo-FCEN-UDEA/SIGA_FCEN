from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class ProgramTypeBase(BaseModel):
    name: str

class ProgramTypeCreate(ProgramTypeBase):
    pass

class ProgramTypeUpdate(BaseModel):
    name: str | None

class ProgramTypeInDB(GeneralResponse, ProgramTypeBase):
    pass