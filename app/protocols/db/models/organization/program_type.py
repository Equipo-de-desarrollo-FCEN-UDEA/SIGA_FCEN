from app.protocols.db.utils.base_model import BaseModel

class ProgramType(BaseModel):
    name: str
    description: str | None