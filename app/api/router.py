from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1.users import user
from app.api.routes.v1.users import rol
from app.api.routes.v1.users import user_rol

from app.api.routes.v1.organization import academic_unit_type
from app.api.routes.v1.organization import academic_unit

from app.api.routes.v1 import auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(ping.router, tags=["ping"])

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(rol.router, prefix="/rol", tags=["rol"])
api_router.include_router(user_rol.router, prefix="/user_rol", tags=["user_rol"])   


api_router.include_router(academic_unit_type.router, prefix="/academic_unit_type", tags=["academic_unit_type"])
api_router.include_router(academic_unit.router, prefix="/academic_unit", tags=["academic_unit"])