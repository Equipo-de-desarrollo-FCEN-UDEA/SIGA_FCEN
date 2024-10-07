from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
from uuid import UUID


class ApplicationStatusType(Enum):
    CREATE = "creada"
    SENT = "enviada"
    APPROVED = "aprobada"
    REJECTED = "rechazada"
    CANCELLED = "cancelada"
    FINISHED = "finalizada"
    IN_COUNCIL = "en consejo"
    IN_INSTITUTE = "en instituto"

class ApplicationStatus(BaseModel):
    name: ApplicationStatusType
    