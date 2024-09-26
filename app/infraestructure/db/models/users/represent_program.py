from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class RepresentProgram(LinkModel):
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="represent_programs")
    
    program_id = Column(ForeignKey("program.id"), primary_key=True)
    program = relationship("Program", back_populates="represent_programs")