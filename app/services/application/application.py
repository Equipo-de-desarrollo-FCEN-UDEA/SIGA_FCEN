from app.services.base import ServiceBase
from app.schemas.application.application import ApplicationCreate, ApplicationUpdate
from app.protocols.db.models.application.application import Application
from app.protocols.db.crud.application.application import CRUDApplicationProtocol

class ApplicationService(ServiceBase[Application, ApplicationCreate, ApplicationUpdate, CRUDApplicationProtocol]):
    pass

application_svc = ApplicationService()