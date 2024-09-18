from pydantic import BaseModel, Field, EmailStr

<<<<<<< HEAD:app/schemas/user.py
from app.schemas.model import GeneralResponse
=======
from app.schemas.utils.base_model import GeneralResponse
>>>>>>> develop:app/schemas/users/user.py


class UserBase(BaseModel):
    email: EmailStr
    names: str | None
    last_names: str | None
    department_id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: str | None
    names: str | None
    last_names: str | None
    department_id: int | None

class UserCreateInDB(UserBase):
    hashed_password: str


class UserInDB(GeneralResponse, UserBase):
    ...


class UserSearch(BaseModel):
    names__icontains: str | None = Field(None, alias="names")
    email__icontains: str | None = Field(None, alias="email")

    class Config:
        allow_population_by_field_name = True