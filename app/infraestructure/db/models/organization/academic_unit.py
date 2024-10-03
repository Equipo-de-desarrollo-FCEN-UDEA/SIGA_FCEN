from sqlalchemy import Column, Uuid, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class AcademicUnit(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True)

    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"), nullable=True)
    academic_unit_type_id = Column(Uuid, ForeignKey("academic_unit_type.id"), nullable=True)

    # relations    
    academic_unit = relationship("AcademicUnit", remote_side="AcademicUnit.id" ,back_populates="academic_units")
    academic_unit_type = relationship("AcademicUnitType", back_populates="academic_units")
    
    roles = relationship("Rol", back_populates="academic_unit")

    academic_units = relationship("AcademicUnit", back_populates="academic_unit", cascade="all, delete-orphan")

    users = relationship("User", secondary="user_rol_academic_unit", back_populates="academic_units")