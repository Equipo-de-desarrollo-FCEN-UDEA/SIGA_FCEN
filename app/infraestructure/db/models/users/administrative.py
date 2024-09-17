from sqlalchemy import Column, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class Administrative(BaseModel):

    user_id = Column (Uuid, ForeignKey("user.id"))
    user = relationship("User", back_populates="administrative")
    academic_unit_id = Column (Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="administrative")
    administrative_type_id = Column(Uuid, ForeignKey("administrative_type.id"))
    administrative_type = relationship("AdministrativeType", back_populates="administrative")