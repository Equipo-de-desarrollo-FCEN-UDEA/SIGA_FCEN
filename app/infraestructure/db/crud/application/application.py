from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.application.application import Application
from app.schemas.application.application import ApplicationCreate, ApplicationUpdate

class ApplicationCrud(CRUDBase[Application, ApplicationCreate, ApplicationUpdate]):
    ...

application_crud = ApplicationCrud(Application)