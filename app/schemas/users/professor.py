from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class ProfessorBase(BaseModel):
    user_id: UUID
    academic_unit_id: UUID
    professor_type_id: UUID
    

class ProfessorCreate(ProfessorBase):
    ...

class ProfessorUpdate(BaseModel):
    ...

class ProfessorDB(GeneralResponse, ProfessorBase):
    ...

