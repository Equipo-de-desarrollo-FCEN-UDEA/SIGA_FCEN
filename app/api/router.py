from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1 import user
from app.api.routes.v1 import rol
from app.api.routes.v1 import user_rol
<<<<<<< HEAD
=======

>>>>>>> feature/reparar


from app.api.routes.v1 import auth

api_router = APIRouter()

api_router.include_router(ping.router, tags=["ping"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(rol.router, prefix="/rol", tags=["rol"])
api_router.include_router(user_rol.router, prefix="/user_rol", tags=["user_rol"])   
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

<<<<<<< HEAD
=======

>>>>>>> feature/reparar


