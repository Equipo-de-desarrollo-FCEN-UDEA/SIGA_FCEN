from sqlalchemy import Column, Uuid, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class VotingStatus(BaseModel):
    voting_id = Column(Uuid, ForeignKey("voting.id"), nullable=False)
    name = Column(String, nullable=False)

    # relations
    voting = relationship("Voting", back_populates="voting_statuses")