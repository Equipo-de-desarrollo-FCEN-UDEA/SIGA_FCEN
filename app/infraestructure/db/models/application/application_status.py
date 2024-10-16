from sqlalchemy import Column, Uuid, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel
from app.protocols.db.models.application.application_status import ApplicationStatusType

class ApplicationStatus(BaseModel):
    user_application_id = Column(Uuid, ForeignKey("user_application.id"), nullable=False)
    status = Column(Enum(ApplicationStatusType), nullable=False)

    # relations
    user_application = relationship("UserApplication", back_populates="application_statuses")