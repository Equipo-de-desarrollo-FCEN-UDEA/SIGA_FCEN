from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

import enum 

# Definir el enum para identification_type
class IdentificationType(enum.Enum):
    PASAPORTE = "pasaporte"
    TARJETA_DE_IDENTIDAD = "tarjeta_de_identidad"
    CEDULA_CIUDADANIA = "cedula_ciudadania"
    CEDULA_EXTRANJERIA = "cedula_extranjeria"


class User(BaseModel):
    name = Column(String(100), nullable=False)
    last_names = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    identification_type= Column(Enum(IdentificationType), nullable=False)
    identification_number= Column(String(10))
    phone = Column(String(10), nullable=True)
    hashed_password = Column(String(300), nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    active = Column(Boolean, nullable=True, default=True)

    # relations
    
    user_rol = relationship("UserRol", back_populates="user")