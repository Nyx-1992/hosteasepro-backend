from sqlalchemy import Column, Integer, String
from database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    guest_name = Column(String)
    check_in = Column(String)
    check_out = Column(String) 
    contact_info = Column(String)
    contacted = Column(Boolean, default=False)