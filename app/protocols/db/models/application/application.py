from enum import Enum
from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class ApplicationStatusType(Enum):
    CREATE = "CREADA"
    SENT = "ENVIADA"
    APPROVED = "APROBADA"
    REJECTED = "RECHAZADA"
    CANCELLED = "CANCELADA"
    FINISHED = "FINALIZADA"
    IN_COUNCIL = "EN CONCEJO"
    IN_INSTITUTE = "EN INSTITUTO"

class Application(BaseModel):
    name: str
    description: str
    academic_unit_id: UUID

