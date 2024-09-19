from pydantic import BaseModel, Field, EmailStr

from app.schemas.utils.base_model import GeneralResponse

from app.infraestructure.db.models.users.user import IdentificationType

class UserBase(BaseModel):
    email: EmailStr
    name: str
    last_name: str
    identification_type: IdentificationType
    identification_number: str
    phone: str | None


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
        allow_population_by_field_name = True