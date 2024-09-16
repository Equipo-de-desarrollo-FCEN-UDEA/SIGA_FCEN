from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class AcademicUnitTypeBase(BaseModel):
    name: str

class AcademicUnitTypeCreate(AcademicUnitTypeBase):
    ...

class AcademicUnitTypeUpdate(BaseModel):
    ...

class AcademicUnitTypeInDB(GeneralResponse, AcademicUnitTypeBase):
    ...