from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

from app.schemas.utils.base_model import GeneralResponse
from app.schemas.users.rol import Rol
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnit

from app.infraestructure.db.models.user.user import IdentificationType

class UserBase(BaseModel):
    email: EmailStr
    name: str
    last_name: str
    identification_type: IdentificationType
    identification_number: str
    phone: str | None
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: str | None
    names: str | None
    last_name: str | None

class UserCreateInDB(UserBase):
    hashed_password: str


class UserInDB(GeneralResponse, UserBase):
    ...


class UserSearch(BaseModel):
    names__icontains: str | None = Field(None, alias="names")
    email__icontains: str | None = Field(None, alias="email")

    class Config:
        populate_by_name = True

class User(UserBase):
    id: UUID
    roles: list[Rol] = []

    class Config:
        orm_mode = True