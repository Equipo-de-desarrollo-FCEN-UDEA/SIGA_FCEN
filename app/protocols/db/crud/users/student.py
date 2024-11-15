from app.protocols.db.crud.base import CRUDProtocol
from app.protocols.db.models.users.student import Student
from app.schemas.users.student import StudentCreate, StudentUpdate

class CRUDStudentProtocol(CRUDProtocol[Student, StudentCreate, StudentUpdate]):
    ...