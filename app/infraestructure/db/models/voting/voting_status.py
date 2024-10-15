from sqlalchemy import Column, Uuid, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel
from app.protocols.db.models.voting.voting_status import VotingStatusType

class VotingStatus(BaseModel):
    voting_id = Column(Uuid, ForeignKey("voting.id"), nullable=False)
    name = Column(Enum(VotingStatusType), nullable=False)

    # relations
    voting = relationship("VotingStatus", back_populates="voting_statuses")