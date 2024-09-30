from sqlalchemy import Column, String, Uuid,ForeignKey

from sqlalchemy.orm import relationship

from app.infraestructure.db.postgres_utils.base_model import BaseModel

class Rol(BaseModel):
    name = Column(String(100), nullable=False)
    scope = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    academic_unit_id = Column(Uuid,ForeignKey("academic_unit.id") ,nullable=False)

# relations
    academic_unit = relationship("AcademicUnit", back_populates="roles")
    user_roles = relationship("UserRol", back_populates="rol")
