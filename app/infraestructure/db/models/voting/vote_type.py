from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class VoteType(BaseModel):
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relations
    votes = relationship("Vote", back_populates="vote_type")