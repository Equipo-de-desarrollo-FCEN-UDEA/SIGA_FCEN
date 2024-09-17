from app.protocols.db.utils.base_model import BaseModel

from uuid import UUID

class Program(BaseModel):
    name: str
    email: str
    academic_unit_id: UUID
    program_type_id: UUID
