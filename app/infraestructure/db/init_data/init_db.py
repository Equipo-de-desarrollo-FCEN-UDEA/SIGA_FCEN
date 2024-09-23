from app.services.crypt import CryptService

from sqalchemy import event

from app.core.config import get_settings

settings= get_settings()

from app.core.logging import get_logger

from app.infraestructure.db.utils import session
from . import base

log = get_logger(__name__)

settings = get_settings()

def init_db() -> None:

    @event.listens_for(base.Base.metadata, 'after_create')
    def recive_after_create(target, connection, tables, **Kw):
        for table in tables:
            log.info(f"Table {table} created")

    @event.listens_for(base.User.__table__, 'after_create')
    def init_user(table, conn, *args, **kwargs):
        from .user import init_users
        for user in init_users:
            db_obj = dict(user)
            db_obj['hashed_password'] = CryptService.get_password_hash(
                db_obj['password'])
            del db_obj['password']
            conn.execute(table.insert().values(**db_obj))
        log.info(f'Usuarios iniciales creados')

    
    base.Base.metadata.create_all(bind=session.engine)

