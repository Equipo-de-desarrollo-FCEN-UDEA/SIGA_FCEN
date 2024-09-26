from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class RepresentAcademicUnit(LinkModel):
    detalle = Column(String(100), nullable=False)
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="represent_academic_units")
    
    academic_unit_id = Column(ForeignKey("academic_unit.id"), primary_key=True)
    academic_unit = relationship("AcademicUnit", back_populates="represent_academic_units")