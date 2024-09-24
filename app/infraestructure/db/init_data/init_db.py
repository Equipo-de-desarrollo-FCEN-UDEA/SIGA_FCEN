from app.infraestructure.security.crypt import crypt
from sqlalchemy import event
from app.core.config import get_settings
from app.core.logging import get_logger
from app.infraestructure.db.utils import session
from app.infraestructure.db.init_data import base


log = get_logger(__name__)

def init_db_log() -> None:

    # Evento para loguear la creación de tablas
    @event.listens_for(base.Base.metadata, 'after_create')
    def receive_after_create(target, connection, tables, **Kw):
        for table in tables:
            log.info(f"Table {table} created")

    @event.listens_for(base.User.__table__, 'after_create')
    def init_user(table, conn, *args, **kwargs):
        from .user import init_user
        for user in init_user:
            db_obj = dict(user)
            db_obj['hashed_password'] = crypt.get_password_hash(
                db_obj['password'])
            del db_obj['password']
            conn.execute(table.insert().values(**db_obj))
        log.info(f'Usuarios iniciales creados')

    

    base.Base.metadata.create_all(bind=session.engine)

