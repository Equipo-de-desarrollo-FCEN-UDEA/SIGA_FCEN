from sqlalchemy import Column, Uuid, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infraestructure.db.utils.base_model import BaseModel

class ApplicationStatus(BaseModel):
    user_application_id = Column(Uuid, ForeignKey("user_application.id"), nullable=False)
    status = Column(String, nullable=False)

    # relations
    user_application = relationship("UserApplication", back_populates="application_statuses")