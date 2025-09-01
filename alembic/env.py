# alembic/env.py
from __future__ import annotations

import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

# -------- Alembic config / logging
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

# -------- Пути: добавляем корень проекта, чтобы работали импорты app.***
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# -------- Загружаем настройки и модели проекта
from app.core.config import settings  # noqa: E402
from app.models.base import Base      # noqa: E402
# ВАЖНО: импортировать МОДУЛИ с моделями, иначе autogenerate их не увидит
from app.models import host, booking, calendar  # noqa: F401,E402

# -------- Метаданные и URL БД
target_metadata = Base.metadata
# Подменяем sqlalchemy.url из .env (через pydantic-settings)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


def run_migrations_offline() -> None:
    """Запуск миграций без подключения к БД (генерация SQL)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Обычный запуск с подключением к БД."""
    engine = create_engine(settings.DATABASE_URL, poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
