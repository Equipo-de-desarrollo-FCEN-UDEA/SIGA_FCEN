from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import relationship, Mapped
from typing import TYPE_CHECKING

from app.infraestructure.db.utils.base_model import BaseModel

import enum 

if TYPE_CHECKING:
    from app.infraestructure.db.models.users.rol import Rol

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
    user_roles = relationship("UserRol", back_populates="user")
    roles: Mapped[list["Rol"]] = relationship("Rol", secondary="user_rol", back_populates="users")

    professor = relationship("Professor", back_populates="user", uselist=False)
    student = relationship("Student", back_populates="user", uselist=False)
    administrative = relationship("Administrative", back_populates="user", uselist=False)