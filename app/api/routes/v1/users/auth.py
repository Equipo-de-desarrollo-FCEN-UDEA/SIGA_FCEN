from typing import Annotated
from fastapi import Body, Depends, APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.errors.base import BaseErrors
from app.schemas.users.user import User, UserUpdate
from app.services.users.user import user_svc
from app.services.jwt import jwt_service
from app.schemas.token import Token
from app.core.config import settings

from app.api.middleware.postgres_db import get_db


router = APIRouter()
user_model = User


@router.post("/access-token")
def login_access_token(response: Response, 
                       form_data: Annotated[OAuth2PasswordRequestForm,Depends()], 
                       db_postgres: Annotated[Session, Depends(get_db)]):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = user_svc.authenticate(
        email=form_data.username,
        password=form_data.password,
        db=db_postgres
    )
    scopes = [role.rol.scope for role in user.user_roles_academic_units]

    access_token = jwt_service.create_access_token(
        data = {"sub": str(user.id), "scopes": scopes}, expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    response.set_cookie(
        key = "access_token",
        value = access_token,
        httponly = True,     # Impide el acceso desde JavaScript
        secure = True,       # Solo en conexiones HTTPS (requiere HTTPS en producción)
        samesite = "Lax",     # Ayuda a prevenir ataques CSRF
        path = "/",
    )

    return {"message": "Login successful"}

## 
@router.post("/activate-account/", response_model = dict)
def activate_account(token:str= Body(...), db_postgres:Session = Depends(get_db),
)-> dict:
    """ Activate account: Params:
        token: str
    """
    email = jwt_service.decode_access_token(token).sub
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user: User = user_svc.get_by_email(email=email, db=db_postgres)
    user.is_active = True
    user_update = UserUpdate.model_validate(user)
    user_svc.update(id=user.id, obj_in=user_update, db=db_postgres)
    return JSONResponse(status_code=200, content = {"msg": "Cuenta activada correctamente"})
