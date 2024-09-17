from app.infraestructure.db.utils.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Uuid
import uuid

class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
