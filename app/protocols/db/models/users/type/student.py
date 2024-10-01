from app.protocols.db.utils.link_model import LinkModel
from uuid import UUID

class Student(LinkModel):
    id_postgres: UUID
    semester: int
    