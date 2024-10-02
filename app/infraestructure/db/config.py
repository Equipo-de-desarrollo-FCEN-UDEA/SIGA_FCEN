#SERVICES
from app.services.users.user import user_svc
from app.services.users.rol import rol_svc
from app.services.users.user_rol import user_rol_svc
from app.services.users.type.student import student_svc
from app.services.users.type.professor import professor_svc
from app.services.users.type.administrative import administrative_svc
from app.services.organization.academic_unit_type import academic_unit_type_svc
from app.services.organization.academic_unit import academic_unit_svc

# CRUD
from app.infraestructure.db.crud.users.user import user_crud
from app.infraestructure.db.crud.users.rol import rol_crud
from app.infraestructure.db.crud.users.user_rol import user_rol_crud
from app.infraestructure.db.crud.users.type.student import student_crud
from app.infraestructure.db.crud.users.type.professor import professor_crud
from app.infraestructure.db.crud.users.type.administrative import administrative_crud
from app.infraestructure.db.crud.organization.academic_unit_type import academic_unit_type_crud
from app.infraestructure.db.crud.organization.academic_unit import academic_unit_crud


from sqlalchemy import event
from app.core.logging import get_logger

log = get_logger(__name__)

#En este archivo lo que hacemos en crear la session en la base de datos

def init_db() -> None:

    user_svc.register_observer(user_crud)
    rol_svc.register_observer(rol_crud)
    user_rol_svc.register_observer(user_rol_crud)
    academic_unit_type_svc.register_observer(academic_unit_type_crud)
    academic_unit_svc.register_observer(academic_unit_crud)
    student_svc.register_observer(student_crud)
    professor_svc.register_observer(professor_crud)
    administrative_svc.register_observer(administrative_crud)


