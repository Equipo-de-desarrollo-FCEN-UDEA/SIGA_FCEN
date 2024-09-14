from app.protocols.db.utils.base_model import BaseModel

class Rol(BaseModel):
    name: str
    description:str | None