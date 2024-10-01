from enum import Enum

from pydantic_settings import BaseSettings

#Esta clase simplemente nos ayudará a entregar el archivo de entorno dependiendo el caso
class AppEnv(Enum):
    Develop: str = "develop"
    Production: str = "production"
    Testing: str = "testing"

class BaseAppSettings(BaseSettings):
    env: AppEnv = AppEnv.Develop
    class Config:
        env_file = ".env"