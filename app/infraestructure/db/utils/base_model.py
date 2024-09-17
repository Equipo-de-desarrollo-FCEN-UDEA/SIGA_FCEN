from app.infraestructure.db.utils.base import Base
from sqlalchemy import Column, Uuid

from uuid import uuid4

class BaseModel(Base):
    __abstract__ = True
    id = Column(Uuid, default=uuid4 ,primary_key=True)