from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class AdministrativeType(BaseModel):
    name = Column (String(100), nullable=False)

    administratives = relationship("Administrative", back_populates="administrative_type")