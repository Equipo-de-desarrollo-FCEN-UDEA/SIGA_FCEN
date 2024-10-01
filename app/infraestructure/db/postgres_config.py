from app.infraestructure.db.postgres_utils.base import Base
from app.infraestructure.db.postgres_utils import session

#User Services
from app.services.users.user import user_svc
from app.services.users.rol import rol_svc
from app.services.users.user_rol import user_rol_svc

#Organization Services
from app.services.organization.academic_unit_type import academic_unit_type_svc
from app.services.organization.academic_unit import academic_unit_svc

#user crud
from app.infraestructure.db.crud.users.user import user_crud
from app.infraestructure.db.crud.users.rol import rol_crud
from app.infraestructure.db.crud.users.user_rol import user_rol_crud

#Organization crud
from app.infraestructure.db.crud.organization.academic_unit_type import academic_unit_type_crud
from app.infraestructure.db.crud.organization.academic_unit import academic_unit_crud


from app.infraestructure.db.postgres_utils import base


from sqlalchemy import event
from app.core.logging import get_logger

log = get_logger(__name__)

#En este archivo lo que hacemos en crear la session en la base de datos

# def init_db() -> None:
"""si es una base de datos en memoria se deben generar los esquemas inmediatamente"""

# @event.listens_for(base.Base.metadata, 'after_create')
# def receive_after_create(target, connection, tables, **Kw):
#         for table in tables:
#             log.info(f"Table {table} created")

    #Base.metadata.create_all(bind=session.engine)

user_svc.register_observer(user_crud)
rol_svc.register_observer(rol_crud)
user_rol_svc.register_observer(user_rol_crud)
academic_unit_type_svc.register_observer(academic_unit_type_crud)
academic_unit_svc.register_observer(academic_unit_crud)


