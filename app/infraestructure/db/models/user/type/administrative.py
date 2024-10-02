from enum import Enum
from uuid import UUID
from odmantic import Field, Model


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

class Administrative(Model):
    id_postgres: UUID = Field(primary_field=True) 
    type: str
    contract: str

