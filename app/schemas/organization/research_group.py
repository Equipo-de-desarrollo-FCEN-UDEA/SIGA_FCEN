from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class ResearchGroupBase(BaseModel):
    name: str
    description: str | None
    email: str | None
    academic_unit_id: str

class ResearchGroupCreate(ResearchGroupBase):
    pass

class ResearchGroupUpdate(BaseModel):
    name: str | None
    description: str | None
    email: str | None
    academic_unit_id: str | None

class ResearchGroupInDB(GeneralResponse, ResearchGroupBase):
    pass