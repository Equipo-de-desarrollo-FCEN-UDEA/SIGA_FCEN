from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
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

class ApplicationStatus(BaseModel):
    user_application_id: UUID
    status: ApplicationStatusType
    