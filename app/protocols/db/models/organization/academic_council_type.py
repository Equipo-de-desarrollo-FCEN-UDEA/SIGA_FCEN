from app.protocols.db.utils.base_model import BaseModel

class AcademicCouncilType(BaseModel):
    name: str
    description: str | None