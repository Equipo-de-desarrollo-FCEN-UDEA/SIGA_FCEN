from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.model import BaseModel


class User(BaseModel):
    email = Column(String(100), unique=True)
    names = Column(String(100), nullable=True)
    last_names = Column(String(100), nullable=True)
    hashed_password = Column(String(300), nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    active = Column(Boolean, nullable=True, default=True)

    # relations
    
    user_rol = relationship("UserRol", back_populates="user")

    