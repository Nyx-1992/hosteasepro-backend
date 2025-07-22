from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(payload: LoginRequest):
    # Temporary logic -- verify against database later
    if payload.email in ["ns.babczyk@live.de", "sn_apt_management@outlook.com"]:
        return {"status": "success", "email": payload.email}
    return {"status": "error", "detail": "Invalid credentials"}