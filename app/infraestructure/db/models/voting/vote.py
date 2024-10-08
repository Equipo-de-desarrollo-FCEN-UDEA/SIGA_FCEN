from sqlalchemy import Column, Uuid, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel
from app.protocols.db.models.voting.vote import VoteType

class Vote(LinkModel):
    
    voting_id = Column(Uuid, ForeignKey("voting.id"), nullable=False, primary_key=True)
    user_id = Column(Uuid, ForeignKey("user.id"), nullable=False, primary_key=True)
    vote = Column(Enum(VoteType), nullable=False)

    # relations
    voting = relationship("Voting", back_populates="votes")
    user = relationship("User", back_populates="votes")