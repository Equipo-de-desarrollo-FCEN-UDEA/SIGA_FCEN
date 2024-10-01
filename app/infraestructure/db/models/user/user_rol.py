from sqlalchemy import Column, Uuid, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class UserRol(LinkModel):
    user_id = Column(Uuid, ForeignKey("user.id"), primary_key=True)
    rol_id = Column(Uuid, ForeignKey("rol.id"), primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="user_roles")
    rol = relationship("Rol", back_populates="user_roles")
