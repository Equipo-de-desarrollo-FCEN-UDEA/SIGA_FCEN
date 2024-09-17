from pydantic import BaseModel

from app.schemas.utils.link_model import GeneralResponse

from uuid import UUID

class AdministrativeBase(BaseModel):
    user_id: UUID
    academic_unit_id: UUID
    administrative_type_id: UUID
    

class AdministrativeCreate(AdministrativeBase):
    ...

class AdministrativeUpdate(BaseModel):
    ...

class AdministrativeDB(GeneralResponse, AdministrativeBase):
    ...

