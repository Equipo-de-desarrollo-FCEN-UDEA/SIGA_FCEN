from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.application.application_status import ApplicationStatus
from app.schemas.application.application_status import ApplicationStatusCreate, ApplicationStatusUpdate

class CRUDApplicationStatusProtocol(CRUDProtocol[ApplicationStatus, ApplicationStatusCreate, ApplicationStatusUpdate]):
    ...