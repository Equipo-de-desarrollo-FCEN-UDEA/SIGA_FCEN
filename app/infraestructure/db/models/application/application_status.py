from sqlalchemy import Column
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel
from app.protocols.db.models.application.application_status import ApplicationStatusType

class ApplicationStatus(BaseModel):
    name = Column(ApplicationStatusType, nullable=False)

    # relations
    user_applications = relationship("UserApplication", back_populates="application_status")