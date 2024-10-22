from app.protocols.db.utils.base_model import BaseModel

class VoteType(BaseModel):
    name: str
    description: str