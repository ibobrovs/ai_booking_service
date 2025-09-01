from sqlalchemy import Column, String, Integer, Boolean, JSON
from .base import Base

class Host(Base):
    __tablename__ = "hosts"
    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True, index=True)
    display_name = Column(String)
    email = Column(String)
    timezone = Column(String, default="Europe/Riga")
    working_hours = Column(JSON, default=dict)  # напр. {"mon":[["09:00","18:00"]], ...}
    meeting_buffer_min = Column(Integer, default=10)
    # ключ для публичного доступа к слотам/бронированию
    public_api_key = Column(String)
