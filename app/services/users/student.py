from app.services.base import ServiceBase
from app.schemas.users.student import StudentCreate, StudentUpdate
from app.protocols.db.models.users.student import Student
from app.protocols.db.crud.users.student import CRUDStudentProtocol

class StudentService(ServiceBase[Student, StudentCreate, StudentUpdate, CRUDStudentProtocol]):
    ...


student_svc = StudentService()