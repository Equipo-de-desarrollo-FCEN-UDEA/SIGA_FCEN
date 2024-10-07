from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.application.application_status import ApplicationStatus
from app.schemas.application.application_status import ApplicationStatusCreate, ApplicationStatusUpdate

class ApplicationStatusCrud(CRUDBase[ApplicationStatus, ApplicationStatusCreate, ApplicationStatusUpdate]):
    ...

application_status_crud = ApplicationStatusCrud(ApplicationStatus)