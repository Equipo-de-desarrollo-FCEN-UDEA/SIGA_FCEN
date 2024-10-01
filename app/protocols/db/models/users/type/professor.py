from typing import Protocol
from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID



class Professor(LinkModel):
    id_postgres: UUID
    type: str