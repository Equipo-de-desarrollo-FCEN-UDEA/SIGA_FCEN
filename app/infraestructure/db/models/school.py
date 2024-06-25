from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

class School(BaseModel):
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    cost_center = Column(Integer, nullable=False)
    email_dean = Column(String(200), nullable=False)
    direction = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)
    dean = Column(String(255), nullable=False)

    #Relations
    departments = relationship("Department", back_populates="school")