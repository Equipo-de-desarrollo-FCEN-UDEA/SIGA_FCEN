from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class AcademicCouncilTypeBase(BaseModel):
    name: str
    description: str | None

class AcademicCouncilTypeCreate(AcademicCouncilTypeBase):
    pass

class AcademicCouncilTypeUpdate(BaseModel):
    name: str | None
    description: str | None

class AcademicCouncilTypeInDB(GeneralResponse, AcademicCouncilTypeBase):
    pass