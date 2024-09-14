from typing import Protocol
from datetime import datetime

class LinkModel(Protocol):
    created_at: datetime
    updated_at: datetime