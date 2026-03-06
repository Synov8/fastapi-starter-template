from sqlmodel import create_engine

from app.config import settings

DB_URL = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"

engine = create_engine(DB_URL)

__all__ = ["engine", "DB_URL"]
