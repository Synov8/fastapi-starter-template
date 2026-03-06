import os
from enum import Enum
from typing import Dict

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


ENV = Environment(os.getenv("ENV", Environment.DEVELOPMENT))

env_file_map: Dict[Environment, str] = {
    Environment.DEVELOPMENT: ".env.development",
    Environment.PRODUCTION: ".env.production",
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file_map[ENV], env_file_encoding="utf-8"
    )

    env: Environment = Environment.DEVELOPMENT
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_host: str = ""
    postgres_db: str = ""
    postgres_port: int = 5432
    app_url: str = ""


settings = Settings()

__all__ = ["settings"]
