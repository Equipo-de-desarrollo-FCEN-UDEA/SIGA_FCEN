from sqlalchemy import Column, Uuid, ForeignKey, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class Application(BaseModel):

    name = Column(String, nullable=False)
    description = Column(String(100), nullable=False)
    academic_unit_id = Column(Uuid,ForeignKey("academic_unit.id") ,nullable=False)

    # relations
    academic_unit = relationship("AcademicUnit", back_populates="applications")
    user_applications = relationship("UserApplication", back_populates="application")
