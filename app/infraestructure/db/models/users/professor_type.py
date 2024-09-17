from sqlalchemy import Column, String
from app.infraestructure.db.utils.base_model import BaseModel

class ProfessorType(BaseModel):
    name = Column (String(100), nullable=False)