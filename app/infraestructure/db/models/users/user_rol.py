from sqlalchemy import Column, Uuid, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class UserRol(LinkModel):
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    rol_id = Column(ForeignKey("rol.id"), primary_key=True)

    user = relationship("User", back_populates="user_roles")
    rol = relationship("Rol", back_populates="users")
