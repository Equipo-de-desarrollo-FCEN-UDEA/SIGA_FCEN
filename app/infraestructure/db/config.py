<<<<<<< HEAD
from app.services.user import user_svc
from app.services.rol import rol_svc
from app.services.user_rol import user_rol_svc



from app.infraestructure.db.crud.user import user_crud
from app.infraestructure.db.crud.rol import rol_crud
from app.infraestructure.db.crud.user_rol import user_rol_crud



=======
from app.services.users.user import user_svc
from app.services.users.rol import rol_svc
from app.services.users.user_rol import user_rol_svc
from app.services.organization.academic_unit_type import academic_unit_type_svc
from app.services.organization.academic_unit import academic_unit_svc

from app.infraestructure.db.crud.users.user import user_crud
from app.infraestructure.db.crud.users.rol import rol_crud
from app.infraestructure.db.crud.users.user_rol import user_rol_crud
from app.infraestructure.db.crud.organization.academic_unit_type import academic_unit_type_crud
from app.infraestructure.db.crud.organization.academic_unit import academic_unit_crud
>>>>>>> develop

from app.infraestructure.db.utils.base_model import BaseModel
from app.infraestructure.db.utils import session



#En este archivo lo que hacemos en crear la session en la base de datos


def init_db() -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""

    BaseModel.metadata.create_all(bind=session.engine)
    user_svc.register_observer(user_crud)
    rol_svc.register_observer(rol_crud)
    user_rol_svc.register_observer(user_rol_crud)
<<<<<<< HEAD
   
 
=======
    academic_unit_type_svc.register_observer(academic_unit_type_crud)
    academic_unit_svc.register_observer(academic_unit_crud)

>>>>>>> develop
