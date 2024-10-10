from sqlalchemy import Column, Uuid, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel
from app.protocols.db.models.voting.voting import VotingStatus

class Voting(BaseModel):  
    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"), nullable=False)
    application_id = Column(Uuid, ForeignKey("application.id"), nullable=False)
    status = Column(Enum(VotingStatus), nullable=False)

    # relations
    academic_unit = relationship("AcademicUnit", back_populates="votings")
    application = relationship("Application", back_populates="votings")
    votes = relationship("Vote", back_populates="voting")