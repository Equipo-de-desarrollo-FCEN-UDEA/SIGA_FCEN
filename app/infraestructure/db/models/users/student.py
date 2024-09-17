from sqlalchemy import Column, String, Uuid, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.infraestructure.db.utils.link_model import LinkModel

class Student(LinkModel):

    user_id = Column (UUID(as_uuid=True), ForeignKey("user.id"), default=uuid.uuid4, primary_key=True)
    user = relationship("User", back_populates="student", uselist=False)

    program_id = Column(UUID(as_uuid=True), ForeignKey("program.id"))
    program = relationship("Program", back_populates="students")

# Queda faltando la relación de program
    