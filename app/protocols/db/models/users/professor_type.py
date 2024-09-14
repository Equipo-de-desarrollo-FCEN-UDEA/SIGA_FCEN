from app.protocols.db.utils.base_model import BaseModel

class ProfessorType(BaseModel):
    name: str
    description: str | None