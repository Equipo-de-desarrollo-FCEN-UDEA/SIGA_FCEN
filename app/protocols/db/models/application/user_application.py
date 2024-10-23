from datetime import datetime
from app.protocols.db.utils.base_model import BaseModel

from uuid import UUID

class UserApplicationStatus():
    name: str
    updated_by: str
    date: datetime

class UserApplication(BaseModel):
    user_id: UUID
    application_id: UUID
