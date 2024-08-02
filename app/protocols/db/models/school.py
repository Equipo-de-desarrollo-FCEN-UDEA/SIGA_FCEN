from app.protocols.db.utils.model import BaseModel

class School(BaseModel):
    name: str
    address: str | None
    phone: str | None
    email: str | None
    website: str | None
    description: str | None
    director: str | None
    cost_center: str