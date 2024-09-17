from sqlalchemy import Column, String,Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class ResearchGroup(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(500), nullable=True)
    email = Column(String(100), nullable=True)

    # relations
    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="research_groups")