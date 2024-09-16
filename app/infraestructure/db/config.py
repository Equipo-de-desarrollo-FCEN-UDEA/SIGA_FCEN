from app.services.users.user import user_svc
from app.services.users.rol import rol_svc
from app.services.users.user_rol import user_rol_svc
from app.services.organization.academic_unit_type import academic_unit_type_svc
from app.services.organization.academic_unit import academic_unit_svc
from app.services.organization.program_type import program_type_svc
from app.services.organization.academic_council_type import academic_council_type_svc
from app.services.organization.academic_council import academic_council_svc
from app.services.organization.program import program_svc
from app.services.organization.research_group import research_group_svc

from app.infraestructure.db.crud.users.user import user_crud
from app.infraestructure.db.crud.users.rol import rol_crud
from app.infraestructure.db.crud.users.user_rol import user_rol_crud
from app.infraestructure.db.crud.organization.academic_unit_type import academic_unit_type_crud
from app.infraestructure.db.crud.organization.academic_unit import academic_unit_crud
from app.infraestructure.db.crud.organization.program_type import program_type_crud
from app.infraestructure.db.crud.organization.academic_council_type import academic_council_type_crud
from app.infraestructure.db.crud.organization.academic_council import academic_council_crud
from app.infraestructure.db.crud.organization.program import program_crud
from app.infraestructure.db.crud.organization.research_group import research_group_crud

from app.infraestructure.db.utils.base_model import BaseModel
from app.infraestructure.db.utils import session

#En este archivo lo que hacemos en crear la session en la base de datos

def init_db() -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""

    BaseModel.metadata.create_all(bind=session.engine)
    user_svc.register_observer(user_crud)
    rol_svc.register_observer(rol_crud)
    user_rol_svc.register_observer(user_rol_crud)

    academic_unit_type_svc.register_observer(academic_unit_type_crud)
    academic_unit_svc.register_observer(academic_unit_crud)

    program_type_svc.register_observer(program_type_crud)
    program_svc.register_observer(program_crud)

    academic_council_type_svc.register_observer(academic_council_type_crud)
    academic_council_svc.register_observer(academic_council_crud)

    research_group_svc.register_observer(research_group_crud)

