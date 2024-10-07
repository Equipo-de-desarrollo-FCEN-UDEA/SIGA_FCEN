from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel
from app.protocols.db.models.application.application_status import ApplicationStatusType

class ApplicationStatus(BaseModel):
    name = Column(Enum(ApplicationStatusType), nullable=False)

    # relations
    user_applications = relationship("UserApplication", back_populates="application_status")