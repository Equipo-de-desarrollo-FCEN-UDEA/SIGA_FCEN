from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class UserAcademicCouncil(LinkModel):
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="user_academic_councils")
    
    academic_council_id = Column(ForeignKey("academic_council.id"), primary_key=True)
    academic_council = relationship("AcademicCouncil", back_populates="user_academic_councils")