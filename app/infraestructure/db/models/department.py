from sqlalchemy import Column, ForeignKey, String, Integer

from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

class Department(BaseModel):
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable=True)
    coord_email = Column(String(100), nullable=False)
    cost_center = Column(String(100), nullable=True)
    director = Column(String(100), nullable=True)

# relations
    users = relationship("User", back_populates="department")

    school_id = Column(Integer, ForeignKey("school.id"), nullable=False)
    school = relationship("School", back_populates="departments")