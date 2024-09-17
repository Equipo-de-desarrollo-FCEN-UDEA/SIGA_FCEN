from sqlalchemy import Column, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.link_model import LinkModel

class Student(LinkModel):

    user_id = Column (Uuid, ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="administrative")

    progrma_id = Column(Uuid, ForeignKey("program.id"))
    program = relationship("Program", back_populates="students")

# Queda faltando la relación de program
    