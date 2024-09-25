from sqlalchemy import Column, Uuid, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class Program(BaseModel):

    # relations
    academic_unit_id = Column(Uuid, ForeignKey("academic_unit.id"))
    academic_unit = relationship("AcademicUnit", back_populates="programs")

    program_type_id = Column(Uuid, ForeignKey("program_type.id"))
    program_type = relationship("ProgramType", back_populates="programs")

    students = relationship("Student", back_populates="program")
    represent_programs = relationship("RepresentProgram", back_populates="program")
