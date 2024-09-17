from sqlalchemy import Column, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class Porfesor(LinkModel):

    user_id = Column (Uuid, ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="professor")
    academic_unit_id = Column (Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="professor")
    professor_type_id = Column(Uuid, ForeignKey("professor_type.id"))
    professor_type = relationship("ProfessorType", back_populates="professor")