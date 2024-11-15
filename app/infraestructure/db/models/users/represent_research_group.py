from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class RepresentResearchGroup(LinkModel):
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="represent_research_groups")
    
    research_group_id = Column(ForeignKey("research_group.id"), primary_key=True)
    research_group = relationship("ResearchGroup", back_populates="represent_research_groups")