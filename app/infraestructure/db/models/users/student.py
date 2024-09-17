from sqlalchemy import Column, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class Student(BaseModel):

    user_id = Column (Uuid, ForeignKey("user.id"))
    user = relationship("User", back_populates="administrative")

# Queda faltando la relación de program
    