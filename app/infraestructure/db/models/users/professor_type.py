from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.infraestructure.db.utils.base_model import BaseModel

class ProfessorType(BaseModel):
    name = Column (String(100), nullable=False)

    professors = relationship("Professor", back_populates="professor_type")