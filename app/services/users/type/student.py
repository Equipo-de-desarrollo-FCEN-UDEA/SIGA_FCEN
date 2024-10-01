from app.services.base import ServiceBase
from app.protocols.db.crud.users.type.student import CRUDStudentProtocol
from app.schemas.users.type.student import StudentCreate, StudentUpdate
from app.protocols.db.models.users.type.student import Student

class StudentService(ServiceBase[Student, StudentCreate, StudentUpdate, CRUDStudentProtocol]):
    ...


student_svc = StudentService()