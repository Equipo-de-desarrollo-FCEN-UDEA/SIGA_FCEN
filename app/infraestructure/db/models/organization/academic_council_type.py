from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class AcademicCouncilType(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    # relations
    academic_councils = relationship("AcademicCouncil", back_populates="academic_council_type")