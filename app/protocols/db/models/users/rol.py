from app.protocols.db.utils.base_model import BaseModel

class Rol(BaseModel):
    name: str
    scope: str
    description:str | None