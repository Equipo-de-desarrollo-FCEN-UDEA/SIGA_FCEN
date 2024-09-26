import logging

from app.core.settings.app import AppSettings


# Aquí indicamos el archivo env que debe buscar cuando se esté en desarrollo
class DevelopAppSettings(AppSettings):
    debug: bool = True
    title: str = "FastAPI OU_University"
    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"