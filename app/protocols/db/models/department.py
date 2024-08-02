from app.protocols.db.utils.model import BaseModel

class Department(BaseModel):
    name: str
    description: str | None
    coord_email: str
    cost_center: str | None
    director: str | None
    school_id: int