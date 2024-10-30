from enum import Enum
from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class ApplicationStatusType(Enum):
    CREATE = "CREADA"
    IN_INSTITUTE = "EN INSTITUTO"
    IN_COMMITEE = "EN COMITE"
    IN_INTERNATIONAL = "EN RELACIONES INTERNACIONALES"
    REJECTED = "RECHAZADA"
    RETURNED = "DEVUELTA"
    IN_DEAN = "EN DECANATURA"
    APPROVED = "APROBADA"

class Application(BaseModel):
    name: str
    description: str
    academic_unit_id: UUID

