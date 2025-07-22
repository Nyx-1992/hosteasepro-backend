from sqlalchemy import Column, Integer, String
from database import Base

class SOP(Base):
    __tablename__ = "sops"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)