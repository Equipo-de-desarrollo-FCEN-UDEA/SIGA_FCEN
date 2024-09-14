from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class Rol(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(100), nullable=False)

# relations
    user_rol = relationship ("UserRol", back_populates="rol")