from typing import Protocol
from datetime import datetime
from uuid import UUID


class BaseModel(Protocol):
    id: UUID
    created_at: datetime
    updated_at: datetime