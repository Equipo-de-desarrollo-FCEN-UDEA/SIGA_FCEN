from sqlalchemy import Column, Uuid, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class UserRol(LinkModel):
    
    observation = Column(String(100), unique=False)
    
    #Relations
    
    user_id = Column(Uuid, ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates ="user_rol")
    rol_id = Column(Uuid, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="user_rol")