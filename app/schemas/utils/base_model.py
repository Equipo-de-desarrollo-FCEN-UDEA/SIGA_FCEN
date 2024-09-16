from datetime import datetime
from typing import TypeVar
from uuid import UUID   

from pydantic import BaseModel


CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ObjInDB = TypeVar("ObjInDB", bound=BaseModel)


class GeneralResponse(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True