from app.protocols.db.utils.base_model import BaseModel

from enum import Enum
from uuid import UUID


class ApplicationType(Enum):
    FULL_TIME = "Dedicacion exclusiva"


class Application(BaseModel):
    name: ApplicationType
    description: str
    academic_unit_id: UUID

