from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ConnectedCalendar(Base):
    __tablename__ = "connected_calendars"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    kind = Column(String)  # "google"
    credentials = Column(JSON)  # токены OAuth
