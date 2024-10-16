from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.services.users.user import user_svc
from app.services.jwt import jwt_service
from app.schemas.token import Token
from app.core.config import settings

from app.api.middleware.postgres_db import get_db


router = APIRouter()


@router.post("/access-token", response_model=Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_postgres = Depends(get_db)):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = user_svc.authenticate(
        email=form_data.username,
        password=form_data.password,
        db=db_postgres
    )
    access_token = jwt_service.create_access_token(
        user.id, expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    response = Token(
        access_token=access_token,
        token_type="bearer",
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES / 24 / 60,
    )
    return response
