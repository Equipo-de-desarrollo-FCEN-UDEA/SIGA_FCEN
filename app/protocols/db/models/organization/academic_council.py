from app.protocols.db.utils.base_model import BaseModel

from uuid import UUID

class AcademicCouncil(BaseModel):
    academic_unit_id: UUID
    academic_council_type_id: UUID