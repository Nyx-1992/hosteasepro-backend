import requests
from ics import Calendar
from models.booking import Booking
from database import SessionLocal

# Define property calendar feeds
feeds = {
    "Speranta Flat": {
        "Airbnb": "https://www.airbnb.com/calendar/ical/1237076374831130516.ics?s=01582d0497e99114aa6013156146cea4&locale=en-GB",
        "Booking.com": "https://ical.booking.com/v1/export?t=8123e217-45b4-403d-8fa0-9dcc65c26800",
        "Lekkeslaap": "https://www.lekkeslaap.co.za/suppliers/icalendar.ics?t=bXEzOHNicTJQT3Nkd1dHb1ZSaXhRUT09"
    },
    "TV House": {
        "Airbnb": "https://www.airbnb.com/calendar/ical/1402174824640448492.ics?s=373c5a71c137230a72f928e88728dcf3&locale=en-GB",
        "Booking.com": "https://ical.booking.com/v1/export?t=ea29c451-4d0b-4fa4-b7a8-e879a33a8940",
        "Lekkeslaap": "https://www.lekkeslaap.co.za/suppliers/icalendar.ics?t=QzZ2aFlFVHhxYnoxdGRVL3ZwelRGUT09"
    }
}

db = SessionLocal()

def parse_calendar(url: str, property_name: str, platform: str):
    response = requests.get(url)
    calendar = Calendar(response.text)
    for event in calendar.events:
        booking = Booking(
            platform=platform,
            guest_name=event.name or "Unknown",
            check_in=str(event.begin.date()),
            check_out=str(event.end.date()),
            contact_info=event.description or "Not provided",
            contacted=False
        )
        db.add(booking)
    db.commit()
    print(f"✅ Imported bookings from {platform} -- {property_name}")

def import_all():
    for property_name, sources in feeds.items():
        for platform, url in sources.items():
            try:
                parse_calendar(url, property_name, platform)
            except Exception as e:
                print(f"❌ Failed to import from {platform} -- {property_name}: {e}")

if __name__ == "__main__":
    import_all()