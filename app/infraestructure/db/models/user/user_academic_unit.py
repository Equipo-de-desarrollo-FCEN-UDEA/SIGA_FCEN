from sqlalchemy import Column, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class UserAcademicUnit(LinkModel):
    user_id = Column(Uuid, ForeignKey("user.id"), primary_key=True)
    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"), primary_key=True)

    user = relationship("User", back_populates="user_academic_units")
    academic_unit = relationship("AcademicUnit", back_populates="user_academic_units")