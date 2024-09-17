from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class AcademicUnitType(BaseModel):
    name = Column(String(100), unique=True, nullable=False)

    # relations
    academic_units = relationship("AcademicUnit", back_populates="academic_unit_type")