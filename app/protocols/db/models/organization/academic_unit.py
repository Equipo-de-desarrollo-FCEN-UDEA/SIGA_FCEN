from app.protocols.db.utils.base_model import BaseModel
from uuid import UUID

class AcademicUnit(BaseModel):
    name :str
    description: str
    email:str
    academic_unit_type_id: UUID
    academic_unit_id: UUID