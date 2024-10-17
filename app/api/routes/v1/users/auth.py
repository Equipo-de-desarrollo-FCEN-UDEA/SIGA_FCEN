from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.services.users.user import user_svc
from app.services.jwt import jwt_service
from app.schemas.token import Token
from app.core.config import settings

from app.api.middleware.postgres_db import get_db


router = APIRouter()


@router.post("/access-token", response_model=Token)
def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_postgres: Annotated[Session, Depends(get_db)]):
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

    response = Token(
        access_token=access_token,
        token_type="bearer",
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES / 24 / 60,
    )
    return response
