from app.protocols.db.utils.link_model import LinkModel
from enum import Enum
from uuid import UUID

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

class Administrative(LinkModel):
    id_postgres: UUID
    type: str
    contract: str

