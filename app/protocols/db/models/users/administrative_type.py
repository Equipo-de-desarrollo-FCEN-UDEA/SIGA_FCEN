from app.protocols.db.utils.base_model import BaseModel

class AdministrativeType(BaseModel):
    name: str
    description: str | None