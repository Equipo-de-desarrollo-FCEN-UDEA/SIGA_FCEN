from sqlalchemy import Column, Uuid, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class UserApplication(BaseModel):
    user_id = Column(Uuid, ForeignKey("user.id"), nullable=False)
    application_id = Column(Uuid, ForeignKey("application.id"), nullable=False)
    application_status_id = Column(Uuid, ForeignKey("application_status.id"),nullable=False)

    # relations
    user = relationship("User", back_populates="user_applications")
    application = relationship("Application", back_populates="user_applications")
    application_status = relationship("ApplicationStatus", back_populates="user_applications")
    user_application_academic_units = relationship("UserApplicationAcademicUnit", back_populates="user_application")