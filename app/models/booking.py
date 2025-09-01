from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Hold(Base):
    __tablename__ = "holds"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    starts_at = Column(DateTime)
    ends_at = Column(DateTime)
    duration_min = Column(Integer)
    client_email = Column(String, nullable=True)
    expires_at = Column(DateTime)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    starts_at = Column(DateTime)
    ends_at = Column(DateTime)
    duration_min = Column(Integer)
    channel = Column(String)  # "meet" | "zoom" | "phone"
    client_name = Column(String)
    client_email = Column(String)
    client_phone = Column(String, nullable=True)
    agenda = Column(String, nullable=True)
    status = Column(String, default="confirmed")  # confirmed | cancelled | rescheduled
    join_url = Column(String, nullable=True)
    ics_uid = Column(String, nullable=True)
