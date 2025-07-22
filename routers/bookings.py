from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/bookings", tags=["Bookings"])

class Booking(BaseModel):
    id: int
    platform: str
    guest_name: str
    check_in: str
    check_out: str

bookings_db: List[Booking] = []

@router.get("/", response_model=List[Booking])
def get_bookings():
    return bookings_db

@router.post("/")
def add_booking(booking: Booking):
    bookings_db.append(booking)
    return {"status": "added", "booking": booking}