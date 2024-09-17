from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class ProgramBase(BaseModel):
    name: str
    email: str
    academic_unit_id: str
    program_type_id: str


class ProgramCreate(ProgramBase):
    pass

class ProgramUpdate(BaseModel):
    name: str | None
    email: str | None

class ProgramInDB(GeneralResponse, ProgramBase):
    pass