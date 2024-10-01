from app.infraestructure.db.crud.mongo_base import CRUDBase
from app.infraestructure.db.models.user.type.student import Student
from app.schemas.users.type.student import StudentCreate, StudentUpdate

class StudentCrud(CRUDBase[Student, StudentCreate, StudentUpdate]):
    ...


student_crud = StudentCrud(Student)