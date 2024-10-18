from app.protocols.db.utils.base_model import BaseModel

from uuid import UUID


class UserApplication(BaseModel):
    user_id: UUID
    application_id: UUID
