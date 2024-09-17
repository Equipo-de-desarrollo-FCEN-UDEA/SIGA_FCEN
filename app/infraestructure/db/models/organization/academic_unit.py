from sqlalchemy import Column, Uuid, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class AcademicUnit(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    # relations
    academic_unit_type_id = Column(Uuid, ForeignKey("academic_unit_type.id"), nullable=True)
    academic_unit_type = relationship("AcademicUnitType", back_populates="academic_units")

    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="academic_unit")

    research_groups = relationship("ResearchGroup", back_populates="academic_unit")
    programs = relationship("Program", back_populates="academic_unit")
    academic_councils = relationship("AcademicCouncil", back_populates="academic_unit")