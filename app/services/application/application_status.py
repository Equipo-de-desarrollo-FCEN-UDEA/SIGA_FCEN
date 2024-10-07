from app.services.base import ServiceBase
from app.schemas.application.application_status import ApplicationStatusCreate, ApplicationStatusUpdate
from app.protocols.db.models.application.application_status import ApplicationStatus
from app.protocols.db.crud.application.application_status import CRUDApplicationStatusProtocol

class ApplicationStatusService(ServiceBase[ApplicationStatus, ApplicationStatusCreate, ApplicationStatusUpdate, CRUDApplicationStatusProtocol]):
    pass

application_status_svc = ApplicationStatusService()