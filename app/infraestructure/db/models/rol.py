from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel

class Rol(BaseModel):
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable=True)
    scope = Column(Integer)

# relations
    user_rol = relationship ("UserRol", back_populates="rol")