from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship, Mapped

from app.infraestructure.db.utils.base_model import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.infraestructure.db.models.users.user import User

class Rol(BaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(100), nullable=False)

# relations
    user_roles = relationship("UserRol", back_populates="rol")
    users: Mapped[list["User"]] = relationship ("User", secondary="user_rol" ,back_populates="roles")