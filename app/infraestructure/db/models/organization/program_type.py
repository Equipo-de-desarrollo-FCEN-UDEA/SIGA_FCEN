from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class ProgramType(BaseModel):
    name = Column(String(100), unique=True, nullable=False)

    # relations
    programs = relationship("Program", back_populates="program_type")