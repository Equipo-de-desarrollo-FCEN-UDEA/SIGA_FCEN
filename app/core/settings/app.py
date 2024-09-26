import logging
from typing import Any, Dict, Optional, Tuple, Union
from pydantic import PostgresDsn, SecretStr, validator, RedisDsn, MongoDsn, AnyHttpUrl
from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    # En esta clase de pydantic nos dedicamos a generar la configuración de la aplicación,
    # pydantic automaticammente leerá las variables de entorno con las que encuentre similitud
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI OU_University"
    version: str = "1.0.0"

    access_token_expires_minutes: int
    reset_password_expire_token: int
    aval_confirm_expire_token: int

    max_connection_count: int = 10
    min_connection_count: int = 10

    secret_key: SecretStr

    DEBUGGER: bool = True

    backend_cors_origins: list[AnyHttpUrl] = []

    @validator("backend_cors_origins", pre=True)
    def assemble_cors_origins(cls, v: Union[str, list[str]]) -> Union[list[str], str]:
            if isinstance(v, str) and not v.startswith("["):
                return [i.strip() for i in v.split(",")]
            elif isinstance(v, (list, str)):
                return v
            raise ValueError(v)
    
    # first_superemployee_correo : str
    first_superemployee_password: str
    first_superemployee_last_names: str
    first_superemployee_names: str
    first_superemployee_email: str
    first_superemployee_identification_number: str
    first_superemployee_department_id: int
    first_superemployee_vinculation_type: str
    first_superemployee_rol_id: int
    decano_fing_password: str
