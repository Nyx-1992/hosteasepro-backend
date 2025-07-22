from fastapi import FastAPI
from dotenv import load_dotenv
import os

from routers import auth, tasks, bookings, sops
from database import Base, engine
from models import user, task, booking, sop

# 🔐 Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# 🚀 FastAPI app instance
app = FastAPI()

# 🗄️ Create DB tables
Base.metadata.create_all(bind=engine)

# 🔗 Register routes
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(bookings.router)
app.include_router(sops.router)

@app.get("/")
def root():
    return {"status": "HostEasePro API running"}