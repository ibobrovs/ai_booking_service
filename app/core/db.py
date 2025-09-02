# app/core/db.py
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Один общий Engine для приложения
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

# Фабрика сессий (то, что нужно импортавать в сиды/роуты)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)

def get_db():
    """Dependency для FastAPI: выдаёт сессию и закрывает её после запроса."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Явно укажем, что модуль экспортирует
__all__ = ["engine", "SessionLocal", "get_db"]
