# scripts/seed_host.py
from __future__ import annotations
from datetime import time
from sqlalchemy import select
from app.core.config import settings
from app.core.db import SessionLocal
from app.models.host import Host

# Пример рабочих часов: Пн–Пт 09:00–18:00, Сб 10:00–14:00, Вс выходной
DEFAULT_WH = {
    "mon": [["09:00", "18:00"]],
    "tue": [["09:00", "18:00"]],
    "wed": [["09:00", "18:00"]],
    "thu": [["09:00", "18:00"]],
    "fri": [["09:00", "18:00"]],
    "sat": [["10:00", "14:00"]],
    "sun": []
}

def main():
    db = SessionLocal()
    try:
        slug = "founder"
        res = db.execute(select(Host).where(Host.slug == slug)).scalar_one_or_none()
        if res:
            print(f"Host '{slug}' уже существует")
            return
        host = Host(
            slug=slug,
            display_name="AI Consulting",
            email="noreply@yourdomain.com",
            timezone="Europe/Riga",
            working_hours=DEFAULT_WH,
            meeting_buffer_min=10,
            public_api_key="dev-public-key"
        )
        db.add(host)
        db.commit()
        print("OK: создан Host 'founder'")
    finally:
        db.close()

if __name__ == "__main__":
    main()
