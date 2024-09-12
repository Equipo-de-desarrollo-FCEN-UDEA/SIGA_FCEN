from app.protocols.db.utils.base_model import BaseModel

from enum import Enum

# Definir el enum para identification_type
class IdentificationType(Enum):
    PASAPORTE = "pasaporte"
    TARJETA_DE_IDENTIDAD = "tarjeta_de_identidad"
    CEDULA_CIUDADANIA = "cedula_ciudadania"
    CEDULA_EXTRANJERIA = "cedula_extranjeria"

class User(BaseModel):
    name: str
    last_name: str
    email: str
    identification_type: IdentificationType
    identification_number:str
    phone:str
    hashed_password: str
    is_active: bool
