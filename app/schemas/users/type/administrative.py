from enum import Enum
from pydantic import BaseModel
from uuid import UUID

from app.schemas.users.user import UserInDB


class AdministrativeType(str, Enum):
    SECRETARIA = "SECRETARIA"
    SECRETARIO = "SECRETARIO"
    ALMACENISTA = "ALMACENISTA"
    COORDINADOR = "COORDINADOR"
    DIRECTOR = "DIRECTOR"

class ContractType(str, Enum):
    CARRERA_ADMINISTRATIVA = "CARRERA_ADMINISTRATIVA"
    LIBRE_NOMBRAMIENTO_REMOSION = "LIBRE_NOMBRAMIENTO_REMOSION"
    PROVISIONAL = "PROVISIONAL"
    TEMPORAL = "TEMPORAL"
    CIS="CIS"

class AdministrativeBase(BaseModel):
    id_postgres: UUID
    type: AdministrativeType
    contract: ContractType

class AdministrativeCreate(AdministrativeBase):
    ... 

class AdministrativeUpdate(BaseModel):
    ...

class AdministrativeInDB(AdministrativeBase):
    ...

class AdministrativeResponse(UserInDB):
    administrative: AdministrativeInDB






