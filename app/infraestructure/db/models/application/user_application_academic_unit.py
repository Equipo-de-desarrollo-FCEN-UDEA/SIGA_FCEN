from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

from uuid import UUID

class UserApplicationAcademicUnit(LinkModel):
    user_application_id = Column(UUID, ForeignKey("user_application.id"), nullable=False, primary_key=True)
    academic_unit_id = Column(UUID, ForeignKey("academic_unit.id"), nullable=False, primary_key=True)

    # relations
    user_application = relationship("UserApplication", back_populates="user_application_academic_units")
    academic_unit = relationship("AcademicUnit", back_populates="user_application_academic_units")