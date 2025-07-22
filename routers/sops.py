from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/sops", tags=["SOPs"])

class SOP(BaseModel):
    id: int
    title: str
    category: str

sops_db: List[SOP] = []

@router.get("/", response_model=List[SOP])
def get_sops():
    return sops_db

@router.post("/")
def add_sop(sop: SOP):
    sops_db.append(sop)
    return {"status": "added", "sop": sop}