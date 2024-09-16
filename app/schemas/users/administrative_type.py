from pydantic import BaseModel

from app.schemas.utils.base_model import GeneralResponse

class AdministrativeTypeBase(BaseModel):
    name:str

class AdministrativeTypeCreate(AdministrativeTypeBase):
    ...

class AdministrativeTypeUpdate(BaseModel):
    ...

class AdministrativeTypeDB(GeneralResponse, AdministrativeTypeBase):
    ...

