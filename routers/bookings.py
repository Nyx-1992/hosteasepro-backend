from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models.booking import Booking

router = APIRouter(prefix="/bookings", tags=["Bookings"])
db = SessionLocal()

class BookingBase(BaseModel):
    id: int
    platform: str
    guest_name: str
    check_in: str
    check_out: str
    contact_info: str
    contacted: bool

# In-memory fallback store if needed
bookings_db: List[BookingBase] = []

@router.get("/", response_model=List[BookingBase])
def get_bookings():
    return db.query(Booking).all()

@router.post("/")
def add_booking(booking: BookingBase):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"status": "added", "booking": booking}

@router.patch("/{booking_id}")
def toggle_contacted(booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        return {"error": "Booking not found"}

    booking.contacted = not booking.contacted
    db.commit()
    db.refresh(booking)
    return {"status": "updated", "contacted": booking.contacted}