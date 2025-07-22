from sqlalchemy import Column, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)  # hashed
    role = Column(String)  # admin or assistant
    is_active = Column(Boolean, default=True)