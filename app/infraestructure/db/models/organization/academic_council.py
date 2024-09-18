from sqlalchemy import Column, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from uuid import UUID

from app.infraestructure.db.utils.base_model import BaseModel

class AcademicCouncil(BaseModel):
    # relations
    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="academic_councils")

    academic_council_type_id = Column(Uuid, ForeignKey("academic_council_type.id"))
    academic_council_type = relationship("AcademicCouncilType", back_populates="academic_councils")

    user_academic_councils = relationship("UserAcademicCouncil", back_populates="academic_council")