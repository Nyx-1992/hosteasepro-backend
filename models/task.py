from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    assigned_to = Column(String, ForeignKey("users.email"))