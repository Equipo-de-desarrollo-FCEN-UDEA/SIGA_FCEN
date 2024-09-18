from sqlalchemy import Column, Uuid, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

<<<<<<< HEAD


class UserRol(BaseModel):
    
    observation = Column(String(100), unique=False)
    
    #Relations
    
    user_id = Column(Uuid, ForeignKey("user.id"))
    user = relationship("User", back_populates ="user_rol")
    rol_id = Column(Uuid, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="user_rol")
=======
class UserRol(LinkModel):
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    rol_id = Column(ForeignKey("rol.id"), primary_key=True)

    user = relationship("User", back_populates="user_roles")
    rol = relationship("Rol", back_populates="user_roles")
>>>>>>> develop
